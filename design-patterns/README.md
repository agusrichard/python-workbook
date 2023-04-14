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

### Solution #3: The Decorator Pattern

- What if we wanted to apply two different filters to the same log? Neither of the above solutions supports multiple filters — say, one filtering by priority and the other matching a keyword.
- Look back at the filters defined in the previous section. The reason we cannot stack two filters is that there’s an asymmetry between the interface they offer and the interface they wrap: they offer a log() method but call their handler’s emit() method. Wrapping one filter in another would result in an AttributeError when the outer filter tried to call the inner filter’s emit().
- If we instead pivot our filters and handlers to offering the same interface, so that they all alike offer a log() method, then we have arrived at the Decorator Pattern:

  ```python
  # The loggers all perform real output.

  class FileLogger:
      def __init__(self, file):
          self.file = file

      def log(self, message):
          self.file.write(message + '\n')
          self.file.flush()

  class SocketLogger:
      def __init__(self, sock):
          self.sock = sock

      def log(self, message):
          self.sock.sendall((message + '\n').encode('ascii'))

  class SyslogLogger:
      def __init__(self, priority):
          self.priority = priority

      def log(self, message):
          syslog.syslog(self.priority, message)

  # The filter calls the same method it offers.

  class LogFilter:
      def __init__(self, pattern, logger):
          self.pattern = pattern
          self.logger = logger

      def log(self, message):
          if self.pattern in message:
              self.logger.log(message)
  ```

- For the first time, the filtering code has moved outside of any particular logger class. Instead, it’s now a stand-alone feature that can be wrapped around any logger we want.
- As with our first two solutions, filtering can be combined with output at runtime without building any special combined classes:

  ```python
  log1 = FileLogger(sys.stdout)
  log2 = LogFilter('Error', log1)

  log1.log('Noisy: this logger always produces output')

  log2.log('Ignored: this will be filtered out')
  log2.log('Error: this is important and gets printed')

  # output
  # Noisy: this logger always produces output
  # Error: this is important and gets printed
  ```

  ```python
  log3 = LogFilter('severe', log2)

  log3.log('Error: this is bad, but not that bad')
  log3.log('Error: this is pretty severe')
  ```

### Solution #4: Beyond the Gang of Four patterns

- Python’s logging module wanted even more flexibility: not only to support multiple filters, but to support multiple outputs for a single stream of log messages.
  - The Logger class that callers interact with doesn’t itself implement either filtering or output. Instead, it maintains a list of filters and a list of handlers.
  - For each log message, the logger calls each of its filters. The message is discarded if any filter rejects it.
  - For each log message that’s accepted by all the filters, the logger loops over its output handlers and asks every one of them to emit() the message.
- Or, at least, that’s the core of the idea. The Standard Library’s logging is in fact more complicated. For example, each handler can carry its own list of filters in addition to those listed by its logger. And each handler also specifies a minimum message “level” like INFO or WARN that, rather confusingly, is enforced neither by the handler itself nor by any of the handler’s filters, but instead by an if statement buried deep inside the logger where it loops over the handlers. The total design is thus a bit of a mess.
- But we can use the Standard Library logger’s basic insight — that a logger’s messages might deserve both multiple filters and multiple outputs — to decouple filter classes and handler classes entirely:

  ```python
  # There is now only one logger.

  class Logger:
      def __init__(self, filters, handlers):
          self.filters = filters
          self.handlers = handlers

      def log(self, message):
          if all(f.match(message) for f in self.filters):
              for h in self.handlers:
                  h.emit(message)

  # Filters now know only about strings!

  class TextFilter:
      def __init__(self, pattern):
          self.pattern = pattern

      def match(self, text):
          return self.pattern in text

  # Handlers look like “loggers” did in the previous solution.

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

- Usage:

  ```python

  f = TextFilter('Error')
  h = FileHandler(sys.stdout)
  logger = Logger([f], [h])

  logger.log('Ignored: this will not be logged')
  logger.log('Error: this is important')
  ```

- In fact, the word “log” has dropped entirely away from the name of the filter class, and for a very important reason: there’s no longer anything about it that’s specific to logging! The TextFilter is now entirely reusable in any context that happens to involve strings. Finally decoupled from the specific concept of logging, it will be easier to test and maintain.
- There’s a crucial lesson here: design principles like Composition Over Inheritance are, in the end, more important than individual patterns like the Adapter or Decorator. Always follow the principle. But don’t always feel constrained to choose a pattern from an official list. The design at which we’ve now arrived is both more flexible and easier to maintain than any of the previous designs, even though they were based on official Gang of Four patterns but this final design is not. Sometimes, yes, you will find an existing Design Pattern that’s a perfect fit for your problem — but if not, your design might be stronger if you move beyond them.

### Dodge: “if” statements
Revisiting Design Pattern in Python

**[⬆ back to top](#list-of-contents)**

<br />

---

## References:

- https://python-patterns.guide/gang-of-four/composition-over-inheritance/
