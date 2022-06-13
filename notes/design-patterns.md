# Design Patterns

<br />

## List of Contents:

### 1. [The Composition Over Inheritance Principle](#content-1)

<br />

---

## Contents:

## [The Composition Over Inheritance Principle](https://python-patterns.guide/gang-of-four/composition-over-inheritance/) <span id="content-1"></span>

### Introduction

> Favor object composition over class inheritance.

### Problem: the subclass explosion

- A crucial weakness of inheritance as a design strategy is that a class often needs to be specialized along several different design axes at once, leading to what the Gang of Four call “a proliferation of classes” in their Bridge chapter and “an explosion of subclasses to support every combination” in their Decorator chapter.
- Imagine a base logging class that has gradually gained subclasses as developers needed to send log messages to new destinations.

  ```python
  import sys
  import syslog

  # The initial class.

  class Logger(object):
      def __init__(self, file):
          self.file = file

      def log(self, message):
          self.file.write(message + '\n')
          self.file.flush()

  # Two more classes, that send messages elsewhere.

  class SocketLogger(Logger):
      def __init__(self, sock):
          self.sock = sock

      def log(self, message):
          self.sock.sendall((message + '\n').encode('ascii'))

  class SyslogLogger(Logger):
      def __init__(self, priority):
          self.priority = priority

      def log(self, message):
          syslog.syslog(self.priority, message)
  ```

- The problem arises when this first axis of design is joined by another. Let’s imagine that log messages now need to be filtered — some users only want to see messages with the word “Error” in them, and a developer responds with a new subclass of Logger:

  ```python
  # New design direction: filtering messages.

  class FilteredLogger(Logger):
      def __init__(self, pattern, file):
          self.pattern = pattern
          super().__init__(file)

      def log(self, message):
          if self.pattern in message:
              super().log(message)

  # It works.

  f = FilteredLogger('Error', sys.stdout)
  f.log('Ignored: this is not important')
  f.log('Error: but you want to see this')
  ```

- The trap has now been laid, and will be sprung the moment the application needs to filter messages but write them to a socket instead of a file. None of the existing classes covers that case. If the developer plows on ahead with subclassing and creates a FilteredSocketLogger that combines the features of both classes, then the subclass explosion is underway.
- The total number of classes will increase geometrically if m and n both continue to grow. This is the “proliferation of classes” and “explosion of subclasses” that the Gang of Four want to avoid.
- The solution is to recognize that a class responsible for both filtering messages and logging messages is too complicated. In modern Object Oriented practice, it would be accused of violating the “Single Responsibility Principle.”

### Solution #1: The Adapter Pattern

- One solution is the Adapter Pattern: to decide that the original logger class doesn’t need to be improved, because any mechanism for outputting messages can be wrapped up to look like the file object that the logger is expecting.
  - So we keep the original Logger.
  - And we also keep the FilteredLogger.
  - But instead of creating destination-specific subclasses, we adapt each destination to the behavior of a file and then pass the adapter to a Logger as its output file.
- Here are adapters for each of the other two outputs:

  ```python
  import socket

  class FileLikeSocket:
      def __init__(self, sock):
          self.sock = sock

      def write(self, message_and_newline):
          self.sock.sendall(message_and_newline.encode('ascii'))

      def flush(self):
          pass

  class FileLikeSyslog:
      def __init__(self, priority):
          self.priority = priority

      def write(self, message_and_newline):
          message = message_and_newline.rstrip('\n')
          syslog.syslog(self.priority, message)

      def flush(self):
          pass
  ```

- Python encourages duck typing, so an adapter’s only responsibility is to offer the right methods — our adapters, for example, are exempt from the need to inherit from either the classes they wrap or from the file type they are imitating. They are also under no obligation to re-implement the full slate of more than a dozen methods that a real file offers. Just as it’s not important that a duck can walk if all you need is a quack, our adapters only need to implement the two file methods that the Logger really uses.
- And so the subclass explosion is avoided! Logger objects and adapter objects can be freely mixed and matched at runtime without the need to create any further classes:

  ```python
  sock1, sock2 = socket.socketpair()

  fs = FileLikeSocket(sock1)
  logger = FilteredLogger('Error', fs)
  logger.log('Warning: message number one')
  logger.log('Error: message number two')

  print('The socket received: %r' % sock2.recv(512))
  ```

- Note that it was only for the sake of example that the FileLikeSocket class is written out above — in real life that adapter comes built-in to Python’s Standard Library. Simply call any socket’s makefile() method to receive a complete adapter that makes the socket look like a file.

### Solution #2: The Bridge Pattern

- The Bridge Pattern splits a class’s behavior between an outer “abstraction” object that the caller sees and an “implementation” object that’s wrapped inside.
- We can apply the Bridge Pattern to our logging example if we make the (perhaps slightly arbitrary) decision that filtering belongs out in the “abstraction” class while output belongs in the “implementation” class.
- As in the Adapter case, a separate echelon of classes now governs writing. But instead of having to contort our output classes to match the interface of a Python file object — which required the awkward maneuver of adding a newline in the logger that sometimes had to be removed again in the adapter — we now get to define the interface of the wrapped class ourselves.
- So let’s design the inner “implementation” object to accept a raw message, rather than needing a newline appended, and reduce the interface to only a single method emit() instead of also having to support a flush() method that was usually a no-op.

  ```python
    # The “abstractions” that callers will see.

    class Logger(object):
        def __init__(self, handler):
            self.handler = handler

        def log(self, message):
            self.handler.emit(message)

    class FilteredLogger(Logger):
        def __init__(self, pattern, handler):
            self.pattern = pattern
            super().__init__(handler)

        def log(self, message):
            if self.pattern in message:
                super().log(message)

    # The “implementations” hidden behind the scenes.

    class FileHandler:
        def __init__(self, file):
            self.file = file

        def emit(self, message):
            self.file.write(message + '\n')
            self.file.flush()

    class SocketHandler:
        def __init__(self, sock):
            self.sock = sock

        def emit(self, message):
            self.sock.sendall((message + '\n').encode('ascii'))

    class SyslogHandler:
        def __init__(self, priority):
            self.priority = priority

        def emit(self, message):
            syslog.syslog(self.priority, message)
  ```

- Abstraction objects and implementation objects can now be freely combined at runtime:

  ```python
  handler = FileHandler(sys.stdout)
  logger = FilteredLogger('Error', handler)

  logger.log('Ignored: this will not be logged')
  logger.log('Error: this is important')
  ```

- This presents more symmetry than the Adapter. Instead of file output being native to the Logger but non-file output requiring an additional class, a functioning logger is now always built by composing an abstraction with an implementation.

**[⬆ back to top](#list-of-contents)**

<br />

---

## References:

- https://python-patterns.guide/gang-of-four/composition-over-inheritance/
