# Testing in Python

<br />

## List of Contents:
### 1. [How To Use unittest to Write a Test Case for a Function in Python](#content-1)
### 2. [Unit Testing in Python](#content-2)
### 3. [Getting Started With Testing in Python](#content-3)



<br />

---

## Contents:

## [How To Use unittest to Write a Test Case for a Function in Python](https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python) <span id="content-1"></span>


### Defining a TestCase Subclass
- TestCase provides the general scaffolding for testing our functions. Let’s consider an example:
  ```python
  import unittest

  def add_fish_to_aquarium(fish_list):
      if len(fish_list) > 10:
          raise ValueError("A maximum of 10 fish can be added to the aquarium")
      return {"tank_a": fish_list}


  class TestAddFishToAquarium(unittest.TestCase):
      def test_add_fish_to_aquarium_success(self):
          actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
          expected = {"tank_a": ["shark", "tuna"]}
          self.assertEqual(actual, expected)
  ```

### Executing a TestCase
- Let’s run that test with the following command:
  ```shell
  python -m unittest test_add_fish_to_aquarium.py
  ```
- TestCase recognizes test methods as any method that begins with test. For example, def test_add_fish_to_aquarium_success(self) is recognized as a test and will be run as such. def example_test(self), conversely, would not be recognized as a test because it does not begin with test. Only methods beginning with test will be run and reported when you run python -m unittest ....

### Test for failures
- Example:
  ```python
  import unittest

  def add_fish_to_aquarium(fish_list):
      if len(fish_list) > 10:
          raise ValueError("A maximum of 10 fish can be added to the aquarium")
      return {"tank_a": fish_list}


  class TestAddFishToAquarium(unittest.TestCase):
      def test_add_fish_to_aquarium_success(self):
          actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
          expected = {"tank_a": ["rabbit"]} # wrong expected value
          self.assertEqual(actual, expected)  # assertion will fail
  ```

### Testing a Function that Raises an Exception
- Example:
  ```python
  import unittest

  def add_fish_to_aquarium(fish_list):
      if len(fish_list) > 10:
          raise ValueError("A maximum of 10 fish can be added to the aquarium")
      return {"tank_a": fish_list}


  class TestAddFishToAquarium(unittest.TestCase):
      def test_add_fish_to_aquarium_success(self):
          actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
          expected = {"tank_a": ["shark", "tuna"]}
          self.assertEqual(actual, expected)

      def test_add_fish_to_aquarium_exception(self):
          too_many_fish = ["shark"] * 25
          with self.assertRaises(ValueError) as exception_context:
              add_fish_to_aquarium(fish_list=too_many_fish)
          self.assertEqual(
              str(exception_context.exception),
              "A maximum of 10 fish can be added to the aquarium"
          )
  ```
- `test_add_fish_to_aquarium_exception` uses the with `self.assertRaises(...)` context manager provided by TestCase to check that add_fish_to_aquarium rejects the inputted list as too long.
- The first argument to self.assertRaises is the Exception class that we expect to be raised—in this case, ValueError.
- The `self.assertRaises` context manager is bound to a variable named `exception_context`. The exception attribute on `exception_context` contains the underlying `ValueError` that add_fish_to_aquarium raised. When we call `str()` on that `ValueError` to retrieve its message, it returns the correct exception message we expected.

### Using the setUp Method to Create Resources
- TestCase also supports a setUp method to help you create resources on a per-test basis.
- `setUp` methods can be helpful when you have a common set of preparation code that you want to run before each and every one of your tests. setUp lets you put all this preparation code in a single place, instead of repeating it over and over for each individual test.
- Example:
  ```python
  import unittest

  class FishTank:
      def __init__(self):
          self.has_water = False

      def fill_with_water(self):
          self.has_water = True

  class TestFishTank(unittest.TestCase):
      def setUp(self):
          self.fish_tank = FishTank()

      def test_fish_tank_empty_by_default(self):
          self.assertFalse(self.fish_tank.has_water)

      def test_fish_tank_can_be_filled(self):
          self.fish_tank.fill_with_water()
          self.assertTrue(self.fish_tank.has_water)
  ```
- Since setUp is run before every individual test method, a new FishTank instance is instantiated for both test_fish_tank_empty_by_default and test_fish_tank_can_be_filled. test_fish_tank_empty_by_default verifies that has_water starts off as False. test_fish_tank_can_be_filled verifies that has_water is set to True after calling fill_with_water().

### Using the tearDown Method to Clean Up Resources
- Example:
  ```python
  import os
  import unittest
  
  class AdvancedFishTank:
      def __init__(self):
          self.fish_tank_file_name = "fish_tank.txt"
          default_contents = "shark, tuna"
          with open(self.fish_tank_file_name, "w") as f:
              f.write(default_contents)
  
      def empty_tank(self):
          os.remove(self.fish_tank_file_name)
  
  
  class TestAdvancedFishTank(unittest.TestCase):
      def setUp(self):
          self.fish_tank = AdvancedFishTank()
  
      def tearDown(self):
          self.fish_tank.empty_tank()
  
      def test_fish_tank_writes_file(self):
          with open(self.fish_tank.fish_tank_file_name) as f:
              contents = f.read()
          self.assertEqual(contents, "shark, tuna")
  ```

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Unit Testing in Python](https://www.datacamp.com/community/tutorials/unit-testing-python) <span id="content-2"></span>


### Introduction
- Unit testing is a software testing method by which individual units of source code are put under various tests to determine whether they are fit for use.
- A unit could be bucketed into various categories:
  - An entire module,
  - An individual function,
  - A complete interface like a class or a method.
- Python's unit testing framework offers various features like:
  - Test automation
  - Sharing of setup and shutdown code for tests
  - Aggregating tests into collections
  - Independence of the tests from the reporting framework


### Simple Unit Test
- Example:
  ```python
  def cuboid_volume(l):
    return (l*l*l)

  length = [2,1.1, -2.5, 2j, 'two']

  for i in range(len(length)):
    print ("The volume of cuboid:",cuboid_volume(length[i]))
  ```
- Now there are three things which are certainly incorrect in the above code:
  - First, the volume of cuboid being negative,
  - Second, the volume of the cuboid is a complex number,
  - Finally, the code resulting in a TypeError since you cannot multiply a string, which is a non-int.
- Unit tests are usually written as a separate code in a different file, and there could be different naming conventions that you could follow.
- You could either write the name of the unit test file as the name of the code/unit + test separated by an underscore or test + name of the code/unit separated by an underscore.
- For example, let's say the above code file name is cuboid_volume.py, then your unit test code name could be cuboid_volume_test.py
- Example:
  ```python
  class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),0)
        self.assertAlmostEqual(cuboid_volume(5.5),166.375)
  ```
- It is important to know that your test methods inside the Class TestCuboid should start with a keyword test.
- Example:
  ```python
  from volume_cuboid import *
  import unittest

  class TestCuboid(unittest.TestCase):
      def test_volume(self):
          self.assertAlmostEqual(cuboid_volume(2),8)
          self.assertAlmostEqual(cuboid_volume(1),1)
          self.assertAlmostEqual(cuboid_volume(0),1)

      def test_input_value(self):
          self.assertRaises(TypeError, cuboid_volume, True)
  ```



**[⬆ back to top](#list-of-contents)**

<br />

---

## [Getting Started With Testing in Python](https://realpython.com/python-testing/) <span id="content-1"></span>

### Testing Your Code
- Exploratory testing is a form of testing that is done without a plan. In an exploratory test, you’re just exploring the application.
- Automated testing is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human.
- Testing multiple components is known as integration testing.
- A major challenge with integration testing is when an integration test doesn’t give the right result. It’s very hard to diagnose the issue without being able to isolate which part of the system is failing.
- A unit test is a smaller test, one that checks that a single component operates in the right way.
- An integration test checks that components in your application operate with each other.
- A unit test checks a small component in your application.
- To write a unit test for the built-in function sum(), you would check the output of sum() against a known output.
  ```python
  >>> assert sum([1, 2, 3]) == 6, "Should be 6"
  ```
- If the result from sum() is incorrect, this will fail with an AssertionError and the message "Should be 6".

### Choosing a Test Runner
- There are many test runners available for Python. The one built into the Python standard library is called unittest.
- The three most popular test runners are:
  - unittest
  - nose or nose2
  - pytest
- unittest:
  - requires that: You put your tests into classes as methods and You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement
  - Example:
    ```python
    import unittest
    
    
    class TestSum(unittest.TestCase):
    
        def test_sum(self):
            self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    
        def test_sum_tuple(self):
            self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
    
    if __name__ == '__main__':
        unittest.main()
    ```
  - If you execute this at the command line, you’ll see one success (indicated with .) and one failure (indicated with F): `python test_sum_unittest.py`
- nose:
  - `nose` is compatible with any tests written using the unittest framework and can be used as a drop-in replacement for the unittest test runner.
  - The development of nose as an open-source application fell behind, and a fork called nose2 was created. If you’re starting from scratch, it is recommended that you use nose2 instead of nose.
  - To get started with nose2, install nose2 from PyPI and execute it on the command line. nose2 will try to discover all test scripts named test*.py and test cases inheriting from unittest.TestCase in your current directory:
  - Install nose2 and us it:
    ```shell
    $ pip install nose2
    $ python -m nose2
    .F
    ======================================================================
    FAIL: test_sum_tuple (__main__.TestSum)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "test_sum_unittest.py", line 9, in test_sum_tuple
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
    AssertionError: Should be 6
    
    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s
    
    FAILED (failures=1)
    ```
- pytest:
  - pytest supports execution of unittest test cases. The real advantage of pytest comes by writing pytest test cases. pytest test cases are a series of functions in a Python file starting with the name test_.
  - Great features:
    - Support for the built-in assert statement instead of using special self.assert*() methods
    - Support for filtering for test cases
    - Ability to rerun from the last failing test
    - An ecosystem of hundreds of plugins to extend the functionality
  - Example:
    ```python
    def test_sum():
        assert sum([1, 2, 3]) == 6, "Should be 6"
    
    def test_sum_tuple():
        assert sum((1, 2, 2)) == 6, "Should be 6"
    ```
    
### Writing Your First Test
- Another implementation of sum function:
  ```python
  def sum(arg):
      total = 0
      for val in arg:
          total += val
      return total
  ```
- It is convention to ensure each file starts with test_ so all test runners will assume that Python file contains tests to be executed.
- Some very large projects split tests into more subdirectories based on their purpose or usage.
- You can import any attributes of the script, such as classes, functions, and variables by using the built-in __import__() function. 
  ```python
  target = __import__("my_sum.py")
  sum = target.sum
  ```
- The benefit of using __import__() is that you don’t have to turn your project folder into a package, and you can specify the file name. This is also useful if your filename collides with any standard library packages.


### How to Write Assertions
- The last step of writing a test is to validate the output against a known response. This is known as an assertion.
- There are some general best practices around how to write assertions:
  - Make sure tests are repeatable and run your test multiple times to make sure it gives the same result every time
  - Try and assert results that relate to your input data, such as checking that the result is the actual sum of values in the sum() example
- When you’re writing tests, it’s often not as simple as looking at the return value of a function. Often, executing a piece of code will alter other things in the environment, such as the attribute of a class, a file on the filesystem, or a value in a database. These are known as side effects and are an important part of testing.
- If you find that the unit of code you want to test has lots of side effects, you might be breaking the Single Responsibility Principle.
- Breaking the Single Responsibility Principle means the piece of code is doing too many things and would be better off being refactored.
- 



**[⬆ back to top](#list-of-contents)**

<br />

---

## References:
- https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python
- https://www.datacamp.com/community/tutorials/unit-testing-python
- https://realpython.com/python-testing/