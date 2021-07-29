# Python Clean Code

</br>

## List of Contents:
### 1. [Handling Errors in Python](#content-1)


</br>

---

## Contents:

## [Handling Errors in Python](https://betterprogramming.pub/handling-errors-in-python-9f1b32952423) <span id="content-1"></span>

### Introduction
- “The greatest mistake is to imagine that we never err.” — Thomas Carlyle
- Errors can fall into several categories: logical errors, generated errors, compile-time errors, and runtime errors. In this article, we’ll focus on handling runtime errors — errors that occur while a program is running.


### Why Do We Need Error Handling?
1. Prevents program from crashing if an error occurs: We don't wan to know the user know that our program crashed unexpectedly. Instead, we notity the users that there is an error.
2. Saves time debugging errors
3. Helps define requirements for the program

### Error-Handling Practices
- Exception handling using try - except and try - except - finally
- Assertions
- When to use expections and assertions

### Catching and Handling Exceptions
- Example usage: </br>
  ```python
  try:
      x = int(input("Please enter a number: "))
      y = 100 / x
  except ValueError:
      print("Error: there was an error")
  except ZeroDivisionError:
      print("Error: 0 is an invalid number")
  except Exception:
      print("Error: another error occurred")
  finally:
      print("Cleanup can go here")
  ```
- `finally` will always run


### Things to look out for when handling exceptions
- If you need to swallow an exception, it's a good reason to re-evaluate your code: </br>
  ```python
  try:
    y = 100 / x
  except ZeroDivisionError:
      pass 
  ```
- Don’t declare new variables inside a try statement that might not be reached. </br>
  ```python
  try:
     y = 100 / x
     z = 23 * y
  except ZeroDivisionError:
     pass
  print(z) # z will be undeclared if an Exception is raised
  ```

### Raising Exceptions
- We can re-raise an exception if we don't know that kind of error caused the exception. </br>
  ```python
  try:
      x = int(input("Please enter a number: "))
      y = 100 / x
  except ValueError:
      print("Error: there was an error")
  except ZeroDivisionError:
      print("Error: 0 is an invalid number")
  except Exception:
      raise
  ```

### User-Defined Exceptions
- Defining our our error: </br>
  ```python
  class CustomError(Exception): 
      def __init__(self, value): 
          self.value = value
      def __str__(self): 
          return "Error: %s" % self.value
  try:
      raise CustomError("something went wrong")
  except CustomError as e:
      print(e)
  # prints "Error: something went wrong"
  ```

### Assertions
- Assertions evaluate an expression to true or false. If the expression is false, python will raise an AssertionError exception.
- Could be used for testing
- Example: </br>
  ```python
  a = 20
  assert a < 10, "something went wrong"
  ```


### So When Should We Use Assertions vs. Exceptions?
- Come down to our use case.
- In my opinion, exceptions should be used when handling external inputs and outputs due to user input, hardware, network, etc.
- Exceptions should be used when you want to gracefully exit a program, log data, and notify the user of why such an error occurred.
- Assertions have a fail-fast approach and should be used to find errors in your code and detect bugs.

</br>

---


## References:

https://betterprogramming.pub/handling-errors-in-python-9f1b32952423