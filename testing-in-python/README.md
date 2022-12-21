# Testing in Python

<br />

## List of Contents:
### 1. [How To Use unittest to Write a Test Case for a Function in Python](#content-1)
### 2. [Unit Testing in Python](#content-2)
### 3. [Getting Started With Testing in Python](#content-3)
### 4. [Pytest - Get Started](#content-4)
### 5. [10 Pytest Best Practices](#content-5)
### 6. [5 Pytest Best Practices for Writing Great Python Tests](#content-6)


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
- TestCase recognizes test methods as any method that begins with test. For example, `def test_add_fish_to_aquarium_success(self)` is recognized as a test and will be run as such. `def example_test(self)`, conversely, would not be recognized as a test because it does not begin with test. Only methods beginning with test will be run and reported when you run `python -m unittest` ....

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
- `test_add_fish_to_aquarium_exception` uses the with `self.assertRaises(...)` context manager provided by TestCase to check that `add_fish_to_aquarium` rejects the inputted list as too long.
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

**[⬆ back to top](#list-of-contents-)**

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



**[⬆ back to top](#list-of-contents-)**

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

### Executing Test Runners
- Snippet:
  ```python
  if __name__ == '__main__':
      unittest.main()
  ```
- Another way is using the unittest command line. Try this:
  ```shell
  python -m unittest test
  ```
- Add verbosity:
  ```shell
  python -m unittest -v test
  ```
- Instead of providing the name of a module containing tests, you can request an auto-discovery using the following:
  ```shell
  python -m unittest discover
  ```
- Lastly, if your source code is not in the directory root and contained in a subdirectory, for example in a folder called src/, you can tell unittest where to execute the tests so that it can import the modules correctly with the -t flag:
  ```shell
  python -m unittest discover -s tests -t src 
  ```

### Advanced Testing Scenarios
- The three basic steps of every test:
  - Create your inputs
  - Execute the code, capturing the output
  - Compare the output with an expected result
- The data that you create as an input is known as a fixture. It’s common practice to create fixtures and reuse them.
- If you’re running the same test and passing different values each time and expecting the same result, this is known as parameterization.
- There’s a special way to handle expected errors. You can use .assertRaises() as a context-manager, then inside the with block execute the test steps:
  ```python
  import unittest
  
  from my_sum import sum
  
  
  class TestSum(unittest.TestCase):
      def test_list_int(self):
          """
          Test that it can sum a list of integers
          """
          data = [1, 2, 3]
          result = sum(data)
          self.assertEqual(result, 6)
  
      def test_list_fraction(self):
          """
          Test that it can sum a list of fractions
          """
          data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
          result = sum(data)
          self.assertEqual(result, 1)
  
      def test_bad_type(self):
          data = "banana"
          with self.assertRaises(TypeError):
              result = sum(data)
  
  if __name__ == '__main__':
      unittest.main()
  ```
### Isolating Behaviors in Your Application
- Avoid having many side effects:
  - Refactoring code to follow the Single Responsibility Principle
  - Mocking out any method or function calls to remove side effects
  - Using integration testing instead of unit testing for this piece of the application 

### Testing Data-Driven Applications
- Here’s an example of that structure if the data consisted of JSON files:
  ```
  project/
  │
  ├── my_app/
  │   └── __init__.py
  │
  └── tests/
      |
      └── unit/
      |   ├── __init__.py
      |   └── test_sum.py
      |
      └── integration/
          |
          ├── fixtures/
          |   ├── test_basic.json
          |   └── test_complex.json
          |
          ├── __init__.py
          └── test_integration.py 
  ```
- Test code:
  ```python
  import unittest
  
  
  class TestBasic(unittest.TestCase):
      def setUp(self):
          # Load test data
          self.app = App(database='fixtures/test_basic.json')
  
      def test_customer_count(self):
          self.assertEqual(len(self.app.customers), 100)
  
      def test_existence_of_customer(self):
          customer = self.app.get_customer(id=10)
          self.assertEqual(customer.name, "Org XYZ")
          self.assertEqual(customer.address, "10 Red Road, Reading")
  
  
  class TestComplexData(unittest.TestCase):
      def setUp(self):
          # load test data
          self.app = App(database='fixtures/test_complex.json')
  
      def test_customer_count(self):
          self.assertEqual(len(self.app.customers), 10000)
  
      def test_existence_of_customer(self):
          customer = self.app.get_customer(id=9999)
          self.assertEqual(customer.name, u"バナナ")
          self.assertEqual(customer.address, "10 Red Road, Akihabara, Tokyo")
  
  if __name__ == '__main__':
      unittest.main()
  ```

**[⬆ back to top](#list-of-contents-)**

<br />

---

## [Pytest - Get Started](https://docs.pytest.org/en/7.2.x/getting-started.html#get-started) <span id="content-4"></span>

### Run multiple tests
- Snippet:
  ```python
  # content of test_sysexit.py
  import pytest
  
  
  def f():
      raise SystemExit(1)
  
  
  def test_mytest():
      with pytest.raises(SystemExit):
          f()
  ```
- Execute the test function with “quiet” reporting mode:
  ```shell
  $ pytest -q test_sysexit.py
  ```
- The -q/--quiet flag keeps the output brief in this and following examples.

### Group multiple tests in a class
- Snippet:
  ```python
  # content of test_class.py
  class TestClass:
      def test_one(self):
          x = "this"
          assert "h" in x
  
      def test_two(self):
          x = "hello"
          assert hasattr(x, "check")
  ```
- pytest discovers all tests following its Conventions for Python test discovery, so it finds both test_ prefixed functions. There is no need to subclass anything, but make sure to prefix your class with Test otherwise the class will be skipped.
- Something to be aware of when grouping tests inside classes is that each test has a unique instance of the class. Having each test share the same class instance would be very detrimental to test isolation and would promote poor test practices.

**[⬆ back to top](#list-of-contents-)**

<br />

---

## [10 Pytest Best Practices](https://climbtheladder.com/10-pytest-best-practices/) <span id="content-5"></span>

### 1. Use assert instead of the assertEquals built-in
- It's pretty much self-explanatory

### 2. Test one thing in each test
- By testing only one thing in each test, it’s much easier to pinpoint which test is failing and why.

### 3. Make tests easy to read and maintain
- Use clear and concise names
- Organize them into logical groups
- Each test only performs a single assertion

### 4. Write short, isolated unit tests
- Isolated unit tests are easier to write, understand, and maintain. They’re also less likely to break when code changes, making them more robust.
- Test one thing at a time
- Unit tests are short, if they are too long and complex. Probably they're doing too much
- This means each test should set up its own data and not depend on any side effects from other tests. Isolation makes tests more reliable and easier to debug.

### 5. Avoid setup and teardown code
- Use fixtures (functions that are called before and after each test)

### 6. Use pytest fixtures for complex set up
- Using fixtures makes your tests more readable and easier to maintain

### 7. Use parametrize for multiple inputs
- If you have a test that needs to be run with different input values, using parametrize allows you to write the test once and then specify the input values as parameters. This is much more efficient than writing separate tests for each input value.
- To use parametrize, simply add @pytest.mark.parametrize as a decorator above your test function, and then specify the input values as arguments.

### 8. Use @pytest.mark decorators to run subsets of tests
- By using @pytest.mark decorators, you can specify which tests should be run in which situations.

### 9. Run only failed tests with –lf or –ff
- If you use –lf or –ff, pytest will only run the failed test (or the first failing test)

### 10. Keep your test suite fast
- There are a few things you can do to keep your test suite fast:
  - Run tests in parallel: This can be done using pytest-xdist or pytest-parallel.
  - Use fixture caching: This can speed up tests that rely on expensive setup operations, such as connecting to a database.
  - Filter out tests that don’t need to be run: You can use pytest’s -k option to specify which tests to run.

**[⬆ back to top](#list-of-contents-)**

<br />

---

## [5 Pytest Best Practices for Writing Great Python Tests](https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/) <span id="content-6"></span>

### Fixtures
- Fixtures are how test setups (and any other helpers) are shared between tests. 
- Fixtures are the basic building blocks that unlock the full power of pytest.
- Some of the most useful fixtures tend to be context fixtures, or yield fixtures.
- The code before the yield is executed as setup for the fixture, while the code after the yield is executed as clean-up. The value yielded is the fixture value received by the user.
- Like all contexts, when yield fixtures depend on each other they are entered and exited in stack, or Last In First Out (LIFO) order. That is, the last fixture to be entered is the first to be exited.
  ```python
  import pytest
  
  @pytest.fixture
  def first():
      print("Set up first fixture")
      yield
      print("Clean up first fixture")
  
  
  @pytest.fixture
  def second(first):
      print("Set up second fixture")
      yield
      print("Clean up second fixture")
  
  
  def test_context_fixture_order(second):
      print("In the test")
      assert False
  ```
  
### Parametrize
- Parametrizing tests and fixtures allows us to generate multiple copies of them easily.
- Parametrizing tests has an obvious use: to test multiple inputs to a function and verify that they return the expected output. It’s really useful to thoroughly test edge cases.
- Parametrizing fixtures is subtly different, incredibly powerful, and a more advanced pattern. It models that wherever the fixture is used, all parametrized values can be used interchangeably. Parametrizing a fixture indirectly parametrizes every dependent fixture and function.

### Lifecycle of a Test Run -- Collection
- During test collection, every test module, test class, and test function that matches certain conditions is picked up and added to a list of candidate tests.
- In parallel, every fixture is also parsed by inspecting conftest.py files as well as test modules.
- Finally, parametrization rules are applied to generate the final list of functions, and their argument (and fixture) values.
- In this phase, the test files are imported and parsed; however, only the meta-programming code – i.e, the code the operates on fixtures and functions – is actually executed. 
- The idea here is that pytest needs to understand all the tests that actually have to execute, and it can’t do that without executing things like parametrize.
- For pytest to resolve and collect all the combinations of fixtures in tests, it needs to resolve the fixture DAG. Therefore, the inter-fixture dependencies are resolved at collection time but none of the fixtures themselves are executed.

### Lifecycle of a Test Run -- Execution
- After test collection has concluded successfully, all collected tests are run.
- But before the actual test code is run, the fixture code is first executed, in order, from the root of the DAG to the end fixtures:
  - session scoped fixtures are executed if they have not already been executed in this test run. Otherwise, the results of previous execution are used.
  - module scoped fixtures are executed if they have not already been executed as part of this test module in this test run. Otherwise, the results of previous execution are used.
  - class scoped fixtures are executed if they have not already been executed as part of this class in this test run. Otherwise, the results of previous execution are used.
  - function scoped fixtures are executed.
- Finally, the test function is called with the values for the fixtures filled in. Note that the parametrized arguments have already been “filled in” as part of collection.

### Patterns and Anti-Patterns
- Prefer mocker over mock
- Parametrize the same behavior, have different tests for different behaviors
- Don’t modify fixture values in other fixtures
- Prefer responses over mocking outbound HTTP requests
- Prefer tmpdir over global test artifacts

### Prefer mocker over mock
- Snippet:
```python
"""Add this to <project-root>/mocker_over_mock.py"""

import pytest

try:
    import mock  # fails on Python 3
except ImportError:
    from unittest import mock


def first_test_fn():
    return 42


def another_test_fn():
    return 42


class TestManualMocking(object):
    """This is dangerous because we could forget to call ``stop``,
    or the test could error out; both would leak state across tests
    """

    @pytest.mark.xfail(strict=True, msg="We want this test to fail.")
    def test_manual(self):
        patcher = mock.patch("mocker_over_mock.first_test_fn", return_value=84)
        patcher.start()
        assert first_test_fn() == 42
        assert False
        patcher.stop()

    def test_manual_follow_up(self):
        assert first_test_fn() == 42, "Looks like someone leaked state!"


class TestDecoratorMocking(object):
    """This is better, but:
        1. Confusing when we start layering ``pytest`` decorators like
        ``@pytest.mark`` with ``@mock.patch``.
        2. Doesn't work when used with fixtures.
        3. Forces you to accept `mock_fn` as an argument even when the
        mock is just set up and never used in your test - more boilerplate.
    """

    @pytest.mark.xfail(strict=True, msg="We want this test to fail.")
    @mock.patch("mocker_over_mock.another_test_fn", return_value=84)
    def test_decorator(self, mock_fn):
        assert another_test_fn() == 84
        assert False

    def test_decorator_follow_up(self):
        assert another_test_fn() == 42

    @pytest.fixture
    @mock.patch("mocker_over_mock.another_test_fn", return_value=84)
    def mock_fn(self, _):
        return

    def test_decorator_with_fixture(self, mock_fn):
        assert another_test_fn() == 84, "@mock and fixtures don't mix!"


class TestMockerFixture(object):
    """This is best; the mocker fixture reduces boilerplate and
    stays out of the declarative pytest syntax.
    """

    @pytest.mark.xfail(strict=True, msg="We want this test to fail.")
    def test_mocker(self, mocker):
        mocker.patch("mocker_over_mock.another_test_fn", return_value=84)
        assert another_test_fn() == 84
        assert False

    def test_mocker_follow_up(self):
        assert another_test_fn() == 42    

    @pytest.fixture
    def mock_fn(self, mocker):
        return mocker.patch("mocker_over_mock.test_basic.another_test_fn", return_value=84)

    def test_mocker_with_fixture(self, mock_fn):
        assert another_test_fn() == 84
```

### Parametrize the same behavior, have different tests for different behaviors
- Parametrize when asserting the same behavior with various inputs and expected outputs. Make separate tests for distinct behaviors. Use ids to describe individual test cases.
- Snippet:
```python
import pytest


def divide(a, b):
    return a / b


@pytest.mark.parametrize("a, b, expected, is_error", [
    (1, 1, 1, False),
    (42, 1, 42, False),
    (84, 2, 42, False),
    (42, "b", TypeError, True),
    ("a", 42, TypeError, True),
    (42, 0, ZeroDivisionError, True),
])
def test_divide_antipattern(a, b, expected, is_error):
    if is_error:
        with pytest.raises(expected):
            divide(a, b)
    else:
        assert divide(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (42, 1, 42),
    (84, 2, 42),
])
def test_divide_ok(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (42, "b", TypeError),
    ("a", 42, TypeError),
    (42, 0, ZeroDivisionError),
])
def test_divide_error(a, b, expected):
    with pytest.raises(expected):
        divide(a, b)
```

### Don’t modify fixture values in other fixtures
- Modify and build on top of fixture values in tests; never modify a fixture value in another fixture – use deepcopy instead.
- For a given test, fixtures are executed only once. However, multiple fixtures may depend on the same upstream fixture. If any one of these modifies the upstream fixture’s value, all others will also see the modified value; this will lead to unexpected behavior.
- Snippet:
```python
from copy import deepcopy

import pytest


@pytest.fixture
def alex():
    return {
        "name": "Alex",
        "team": "Green",
    }


@pytest.fixture
def bala(alex):
    alex["name"] = "Bala"
    return alex


@pytest.fixture
def carlos(alex):
    _carlos = deepcopy(alex)
    _carlos["name"] = "Carlos"
    return _carlos


def test_antipattern(alex, bala):
    assert alex == {"name": "Alex", "team": "Green"}
    assert bala == {"name": "Bala", "team": "Green"}


def test_pattern(alex, carlos):
    assert alex == {"name": "Alex", "team": "Green"}
    assert carlos == {"name": "Carlos", "team": "Green"}
```

### Prefer responses over mocking outbound HTTP requests
- Never manually create Response objects for tests; instead use the responses library to define what the expected raw API response is.
- You can read the README of responses for the examples

### Prefer tmpdir over global test artifacts
- Don’t create files in a global tests/artifacts directory for every test that needs a file-system interface. Instead, use the tmpdir fixture to create files on-the-fly and pass those in.
- Global artifacts are removed from the tests that use them, which makes them difficult to maintain. They’re also static and can’t leverage fixtures and other great techniques. Creating files from fixture data just before a test is run provides a cleaner dev experience.
- Snippet:
  ```python
  import pytest
  
  
  def process_file(fp):
      """Toy function that returns an array of line lengths."""
      return [len(l.strip()) for l in fp.readlines()]
  
  
  @pytest.mark.parametrize("filename, expected", [
      ("first.txt", [3, 3, 3]),
      ("second.txt", [5, 5]),
  ])
  def test_antipattern(filename, expected):
      with open("resources/" + filename) as fp:
          assert process_file(fp) == expected
  
  
  @pytest.mark.parametrize("contents, expected", [
      ("foo\nbar\nbaz", [3, 3, 3]),
      ("hello\nworld", [5, 5]),
  ])
  def test_pattern(tmpdir, contents, expected):
      tmp_file = tmpdir.join("testfile.txt")
      tmp_file.write(contents)
      with tmp_file.open() as fp:
          assert process_file(fp) == expected
  ```
  
### Bonus: A Word of Caution
- I always ask myself these questions before writing a test:
  - Am I testing the code as frozen in time, or testing the functionality that lets underlying code evolve?
  - Am I testing my functionality, or the language constructs themselves?
  - Is the cost of writing and maintaining this test more than the cost of the functionality breaking?
- 

**[⬆ back to top](#list-of-contents-)**

<br />

---

## References:
- https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python
- https://www.datacamp.com/community/tutorials/unit-testing-python
- https://realpython.com/python-testing/
- https://docs.pytest.org/en/7.2.x/getting-started.html#get-started
- https://climbtheladder.com/10-pytest-best-practices/
- https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/