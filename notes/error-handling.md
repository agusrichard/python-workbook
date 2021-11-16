# Python Clean Code

<br />

## List of Contents:
### 1. [Handling Errors in Python](#content-1)
### 2. [Stop Using Exceptions Like This in Python](#content-2)
### 3. [In Python, Don’t Look Before You Leap](#content-3)


<br />

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
- Example usage: <br />
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
- If you need to swallow an exception, it's a good reason to re-evaluate your code: <br />
  ```python
  try:
    y = 100 / x
  except ZeroDivisionError:
      pass 
  ```
- Don’t declare new variables inside a try statement that might not be reached. <br />
  ```python
  try:
     y = 100 / x
     z = 23 * y
  except ZeroDivisionError:
     pass
  print(z) # z will be undeclared if an Exception is raised
  ```

### Raising Exceptions
- We can re-raise an exception if we don't know that kind of error caused the exception. <br />
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
- Defining our our error: <br />
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
- Example: <br />
  ```python
  a = 20
  assert a < 10, "something went wrong"
  ```


### So When Should We Use Assertions vs. Exceptions?
- Come down to our use case.
- In my opinion, exceptions should be used when handling external inputs and outputs due to user input, hardware, network, etc.
- Exceptions should be used when you want to gracefully exit a program, log data, and notify the user of why such an error occurred.
- Assertions have a fail-fast approach and should be used to find errors in your code and detect bugs.

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Stop Using Exceptions Like This in Python](https://betterprogramming.pub/handling-errors-in-python-9f1b32952423) <span id="content-2"></span>


### Introduction
- Exception handling means deciding what to do with interruptions.
- Basic example:
  ```python
  raise ValueError("Something has gone wrong.")
  ```

### 1. Avoid Bare except
- The first rule of thumb is to absolutely avoid using bare except, as it doesn't give us any exceptions object to inspect.
- Furthermore, using bare except also catches all exceptions, including exceptions that we generally don’t want, such as SystemExit or KeyboardInterrupt.
- Example:
  ```python
  #Do NOT ever use bare exception
  try:
      return fetch_all_books()

  except:  # !!!
      raise
  ```
- What's wrong with catching exceptions:
  - Catching every exception could cause our application to fail without us really knowing why.
  - Example:
    ```python
    def upload_proof_of_address_doc(file):
    try:
        result = upload_pdf_to_s3(file)
        if not result:
            raise Exception("File not found!")

    except:
        raise
    ```
  - Look at the above code, no matter what kind of reasons behind failure to upload the pdf, we always get the same error which is file not found.

### 2. Stop Using raise Exception
- We should avoid raising a generic Exception in Python because it tends to hide bugs.
- Example:
  ```python
  # Do NOT raise a generic Exception:

  def get_book_List():
      try:
          if not fetch_books():
              raise Exception("This exception will not be caught by specific catch")  # !!!

      except ValueError as e:
          print("This doesn't catch Exception")
          raise


  get_book_List()
  # Exception: general exceptions not caught by specific handling
  ```
- While there are plenty of ways to write bad code, this is one of the worst anti-patterns (known as error hiding).


### 3. Stop Using except Exception
- Example:
  ```python
  # Do NOT catch with a generic Exception:

  def fetch_all_books():
      try:
          if not fetch_all_books():
              raise DoesNotExistError("No books found!")

      except Exception as e:  # !!!
          print(e)
          raise
  ```
- However, the caveat is that developers tend to catch exceptions with a generic BaseException or Exception class.
- In this scenario, it means that we will catch everything. Everything including exceptions that we cannot or perhaps should not recover from.
- We should always plan ahead and figure out what can break and what exceptions are expected to be thrown.
- We can throw a custom UserDoesNotExist error when we can't find a correct user profile by email.
- Example of defining custom error exception:
  ```python
  class UserDoesNotExist(Exception):
      """Raised when user does not exist"""
      pass
  ```
- Before writing our own custom user-defined exceptions, we should always check if the library that we are using has its own built-in exceptions that meet our use case.
- Example of how to properly handle an exception:
  ```python
  # Do:

  def fetch_user_profile(id):
      try:
          user = get_user_profile(id)
          if not user:
              raise UserDoesNotExist("User does not exist.")  # Raise specific exception

      except UserDoesNotExist as e:  # Catch specific exception
          logger.exception(e)  # Logs the exception
          raise  # Just raise
          # raise UserDoesNotExist # Don't do this or you'll lose the stack trace
  ```

### 4. Refrain From Passing in except Blocks
- However, the worst possible thing a developer can do is the following:
  ```python
  # Do NOT ever pass a bare exception:
  try:
      compute_combination_sum(value)

  except:
      pass


  # Do NOT do this:
  try:
      compute_combination_sum(value)

  except BaseException:
      pass
  ```
- The code above implies that despite the fact that we are not ready for any exceptions, we are catching any exceptions willingly.
- Another disadvantage of passing and catching Exception (or bare except) is that we will never know the second error when there are two errors in the code. The first error will always be caught first and we will get out of the try block.
- If we’re just passing an except statement, it’s a good sign that we aren’t really prepared for the exception that we are catching.


### Log, don’t pass
- Nevertheless, if we don’t have to do anything about the exception, we should at least use a more specific exception while also logging the exception.
- Example:
  ```python
  import logging

  logger = logging.getLogger(__name__)


  try:
      parse_number(value)

  except ValueError as e:
      logger.exception(e)
  ```

### Closing Thoughts
- Never use bare except.
- Stop raising generic Exception.
- Stop catching generic Exception.
- Refrain from passing in except blocks.
- In most situations, it’s often better for the app to fail at the point of an exception rather than having our app continue to behave in weird unexpected ways.


## [In Python, Don’t Look Before You Leap](https://betterprogramming.pub/in-python-dont-look-before-you-leap-cff250881930) <span id="content-3"></span>

### Look Before You Leap
- LBYL is the traditional programming style in which we check if a piece of code is going to work before actually running it.
- In other words, if a piece of code needs some prerequisites, we place conditional statements such that the code only runs if all the prerequisites are met.
- Snippet:
  ```python
  person = {'name': 'John Doe', 'age':30, 'gender': 'male'}
  
  #LBYL
  if 'name' in person and 'age' in person and 'gender' in person:
      print("{name} is a {age} year old {gender}.".format(**person))
  else:
      print("Some keys are missing")
  ```

### Easier To Ask for Forgiveness Than Permission
- In this approach, we simply run our code, hoping for the best while being prepared to handle any errors if the code fails.
- Typically, this means enclosing our code in try-except blocks and handling any exceptions that might occur.
- Snippet:
  ```python
  person = {'name': 'John Doe', 'age':30, 'gender': 'male'}
  
  #EAFP
  try:
      print("{name} is a {age} year old {gender}.".format(**person))
  except KeyError:
      print("Some keys are missing")
  ```

### So, Which One’s Better?
- As a rule of thumb, EAFP is considered more Pythonic and should be preferred in most scenarios.
- Here are some reasons why EAFP is preferred over LBYL.
  - Explicit and more readable
    - EAFP makes the “happy path” more explicit and readable. “Explicit is better than implicit” is an important tenet of Python.
    - In the example above, we expect that the keys will be present in the dictionary in most cases, which is what the EAFP code suggests. 
    - The LBYL code, however, emphasizes the rare case where the keys are missing.
  - Better performance
    - EAFP is usually faster than LBYL — especially when lots of checks are needed.
    - Calling the dictionary thrice is time-consuming and repetitive.
    - It’s true that exceptions are costlier than if statements.
    - Exceptions are only triggered a few times, whereas an if statement is always executed.
  - Prevents race conditions
    - Most importantly, EAFP helps us avoid race conditions. Race conditions occur when multiple threads are trying to access an object.
    - Consider two threads trying to access the person dictionary in the LBYL scenario. If one of the threads deletes a key from the dictionary and the second thread is past the checks, we’ll get an exception when the print statement is executed.

### There are some scenarios where using LBYL does make more sense.
- Complex side effects
  - Suppose you begin writing to a file and get an exception when some changes have been made. Trying to revert the changes in the except block can be tricky.
  - Using LBYL to stop the operation beforehand will make your life much easier.
- Too many exceptions
  - If you expect exceptions to be thrown at multiple points in your code, using EAFP might diminish your ability to trace where the code actually failed. Ideally, you should refactor your code to have narrow try-except blocks and continue to use EAFP.



**[⬆ back to top](#list-of-contents)**

<br />

---
## References:
- https://betterprogramming.pub/handling-errors-in-python-9f1b32952423
- https://betterprogramming.pub/stop-using-exceptions-like-this-in-python-2bd8ba7d8841
- https://betterprogramming.pub/in-python-dont-look-before-you-leap-cff250881930