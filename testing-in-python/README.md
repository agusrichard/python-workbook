# Testing in Python

</br>

## List of Contents:
### 1. [How To Use unittest to Write a Test Case for a Function in Python](#content-1)
### 2. [Unit Testing in Python](#content-2)



</br>

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

</br>

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

</br>

---

## References:
- https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python
- https://www.datacamp.com/community/tutorials/unit-testing-python