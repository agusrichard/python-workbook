# Mocking in Python

<br />

## List of Contents:

### 1. [What the mock? — A cheatsheet for mocking in Pythone](#content-1)

<br />

---

## Contents:

## [What the mock? — A cheatsheet for mocking in Python](https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832) <span id="content-1"></span>

### The Mock class in a nutshell

- The centerpoint of the unittest.mock module is, of course, the Mock class.
- The main characteristic of a Mock object is that it will return another Mock instance when:
  - accessing one of its attributes
  - calling the object itself
- Code:

  ```python
  from unittest import mock

  m = mock.Mock()
  assert isinstance(m.foo, mock.Mock)
  assert isinstance(m.bar, mock.Mock)
  assert isinstance(m(), mock.Mock)
  assert m.foo is not m.bar is not m()
  ```

- This is the default behaviour, but it can be overridden in different ways. For example you can assign a value to an attribute in the Mock by:
  - Assign it directly, like you’d do with any Python object.
  - Use the configure_mock method on an instance.
  - Or pass keyword arguments to the Mock class on creation.
- Code:

  ```python
  m.foo = 'bar'
  assert m.foo == 'bar'

  m.configure_mock(bar='baz')
  assert m.bar == 'baz'
  ```

- To override calls to the mock you’ll need to configure its return_value property, also available as a keyword argument in the Mock initializer. The Mock will always return the same value on all calls, this, again, can also be configured by using the side_effect attribute:
  - if you’d like to return different values on each call you can assign an iterable to side_effect.
  - If you’d like to raise an exception when calling the Mock you can simply assign the exception object to side_effect.
- Code:

  ```python
  m.return_value = 42
  assert m() == 42

  m.side_effect = ['foo', 'bar', 'baz']
  assert m() == 'foo'
  assert m() == 'bar'
  assert m() == 'baz'
  try:
      m()
  except StopIteration:
      assert True
  else:
      assert False

  m.side_effect = RuntimeError('Boom')
  try:
      m()
  except RuntimeError:
      assert True
  else:
      assert False
  ```

- Code:
  ```python
  m.assert_called()
  try:
      m.assert_called_once()
  except AssertionError:
      assert True
  else:
      assert False
  ```
- Note in our example assert_called_once failed, this showcases another key aspect of Mock objects, they record all interactions with them and you can then inspect these interactions.
- For example you can use call_count to retrieve the number of calls to the Mock, and use call_args or call_args_list to inspect the arguments to the last or all calls respectively.
- If this is inconvenient at any point you can use the reset_mock method to clear the recorded interactions, note the configuration will not be reset, just the interactions.
- Code:

  ```python
  try:
      m(1, foo='bar')
  except RuntimeError:
      assert True
  else:
      assert False
  assert m.call_args == mock.call(1, foo='bar')
  assert len(m.call_args_list) > 1

  m.reset_mock()
  assert m.call_args is None
  ```

- Finally, let me introduce MagicMock, a subclass of Mock that implements default magic or dunder methods. This makes MagicMock ideal to mock class behaviour, which is why it’s the default class when patching.

### Patch on import

- The main way to use unittest.mock is to patch imports in the module under test using the patch function.
- patch will intercept import statements identified by a string (more on that later), and return a Mock instance you can preconfigure using the techniques we discussed above.
- Code:

  ```python
  # Actual code
  import os

  def work_on():
      path = os.getcwd()
      print(f'Working on {path}')
      return path
  ```

- As mentioned above we need to supply patch with a string representing our specific import. We do not want to supply simply os.getcwd since that would patch it for all modules, instead we want to supply the module under test’s import of os , i.e. work.os . When the module is imported patch will work its magic and return a Mock instead.
- Code:

  ```python
  from unittest import TestCase, mock

  from work import work_on


  class TestWorkMockingModule(TestCase):

      def test_using_context_manager(self):
          with mock.patch('work.os') as mocked_os:
              work_on()
              mocked_os.getcwd.assert_called_once()
  ```

- Using decorator:
  ```python
  @mock.patch('work.os')
  def test_using_decorator(self, mocked_os):
      work_on()
      mocked_os.getcwd.assert_called_once()
  ```
- patch will forward keyword arguments to the Mock class, so to configure a return_value we simply add it as one:
  ```python
  def test_using_return_value(self):
      """Note 'as' in the context manager is optional"""
      with mock.patch('work.os.getcwd', return_value='testing'):
          assert work_on() == 'testing'
  ```

### Mocking classes

- Code:

  ```python
  import os


  class Helper:

      def __init__(self, path):
          self.path = path

      def get_path(self):
          base_path = os.getcwd()
          return os.path.join(base_path, self.path)


  class Worker:

      def __init__(self):
          self.helper = Helper('db')

      def work(self):
          path = self.helper.get_path()
          print(f'Working on {path}')
          return path
  ```

- In order to test Worker in complete isolation we need to patch the whole Helper class:

  ```python
  from unittest import TestCase, mock

  from worker import Worker, Helper


  class TestWorkerModule(TestCase):

      def test_patching_class(self):
          with mock.patch('worker.Helper') as MockHelper:
              MockHelper.return_value.get_path.return_value = 'testing'
              worker = Worker()
              MockHelper.assert_called_once_with('db')
              self.assertEqual(worker.work(), 'testing')
  ```

### Class speccing

- A consequence of the flexibility of Mock is that once we’ve mocked a class Python will not raise AttributeError as it simply will return new instances of MagicMock for basically everything. This is usually a good thing but can lead to some confusing behaviour and potentially bugs. For instance writing the following test,
  ```python
  def test_patching_class_with_typo(self):
      with mock.patch('worker.Helper') as MockHelper:
          MockHelper.return_value.get_path.return_value = 'testing'
          worker = Worker()
          MockHelper.assrt_called_once_with('db')  # erm....
          self.assertEqual(worker.work(), 'testing')
  ```
- will silently pass with no warning completely missing the typo in assrt_called_once .
- Additionally, if we were to rename Helper.get_path to Helper.get_folder, but forget to update the call in Worker our tests will still pass:

  ```python
  import os


  class Helper:

      def __init__(self, path):
          self.path = path

      def get_folder(self):
          base_path = os.getcwd()
          return os.path.join(base_path, self.path)


  class Worker:

      def __init__(self):
          self.helper = Helper('db')

      def work(self):
          path = self.helper.get_path()
          print(f'Working on {path}')
          return path
  ```

- Code:

  ```python
  from unittest import TestCase, mock

  from worker import Worker, Helper


  class TestWorker(TestCase):

      def test_patching_class(self):
          # this test will give a false positive,
          # there is not `get_path` method but we've mocked it
          with mock.patch('worker.Helper') as MockHelper:
              MockHelper.return_value.get_path.return_value = 'testing'
              worker = Worker()
              MockHelper.assert_called_once_with('db')
              self.assertEqual(worker.work(), 'testing')
  ```

- Put simply, it preconfigures mocks to only respond to methods that actually exist in the spec class. There are several ways to define specs, but the easiest is to simply pass autospec=True to the patch call, which will configure the Mock to behave as the object being mocked, raising exceptions for missing attributes and incorrect signatures as required. For example:
  ```python
  def test_patching_class_with_spec(self):
      with mock.patch('worker.Helper', autospec=True) as MockHelper:
          # the following would raise attribute error
          # MockHelper.return_value.get_path.return_value = 'testing'
          MockHelper.return_value.get_folder.return_value = 'testing'
          worker = Worker()
          MockHelper.assert_called_once_with('db')
          # this test will fail since we we're still using `get_path`
          self.assertEqual(worker.work(), 'testing')
  ```

### Partial class mocking

- If you’re less inclined to testing in complete isolation you can also partially patch a class using patch.object:

  ```python
  from unittest import TestCase, mock

  from worker import Worker, Helper


  class TestWorker(TestCase):

      def test_partial_patching(self):
          with mock.patch.object(Helper, 'get_path', return_value='testing'):
              worker = Worker()
              self.assertEqual(worker.helper.path, 'db')
              self.assertEqual(worker.work(), 'testing')
  ```

- Here patch.object is allowing us to configure a mocked version of get_path only, leaving the rest of the behaviour untouched. Of course this means the test is no longer what you would strictly consider a unit test but you may be ok with that.

### Mocking built-in functions and environment variables

- Code:

  ```python
  import os


  def work_on_env():
      path = os.path.join(os.getcwd(), os.environ['MY_VAR'])
      print(f'Working on {path}')
      return path
  ```

  ```python
  from unittest import TestCase, mock

  from worker import work_on_env

  class TestBuiltin(TestCase):

      def test_patch_dict(self):
          with mock.patch('worker.print') as mock_print:
              with mock.patch('os.getcwd', return_value='/home/'):
                  with mock.patch.dict('os.environ', {'MY_VAR': 'testing'}):
                      self.assertEqual(work_on_env(), '/home/testing')
  ```

  ```python
  @mock.patch('os.getcwd', return_value='/home/')
  @mock.patch('worker.print')
  @mock.patch.dict('os.environ', {'MY_VAR': 'testing'})
  def test_patch_builtin_dict_decorators(self, mock_print, mock_getcwd):
      self.assertEqual(work_on_env(), '/home/testing')
      mock_print.assert_called_once_with('Working on /home/testing')
  ```

### Mocking context managers

- Code:

  ```python
  def size_of():
      with open('text.txt') as f:
          contents = f.read()

      return len(contents)
  ```

  ```python
  from io import StringIO
  from unittest import TestCase, mock

  from worker import size_of

  class TestContextManager(TestCase):

      def test_context_manager(self):
          with mock.patch('worker.open') as mock_open:
              mock_open.return_value.__enter__.return_value = StringIO('testing')
              self.assertEqual(size_of(), 7)
  ```

### Mocking class attributes

- Code:

  ```python
  class Pricer:

      DISCOUNT = 0.80

      def get_discounted_price(self, price):
          return price * self.DISCOUNT
  ```

- You could test the code without any mocks in two ways:
  - If the code under test accesses the attribute via self.ATTRIBUTE, which is the case in this example, you can simply set the attribute directly in the instance. This is fairly safe as the change is limited to this single instance.
  - Alternatively you can also set the attribute in the imported class in the test before creating an instance. This however changes the class attribute you’ve imported in your test which could affect the following tests, so you’d need to remember to reset it.
- Code:

  ```python
  from unittest import TestCase, mock, expectedFailure

  from pricer import Pricer


  class TestClassAttribute(TestCase):

      def test_patch_instance_attribute(self):
          pricer = Pricer()
          pricer.DISCOUNT = 0.5
          self.assertAlmostEqual(pricer.get_discounted_price(100), 50.0)

      def test_set_class_attribute(self):
          Pricer.DISCOUNT = 0.75
          pricer = Pricer()
          self.assertAlmostEqual(pricer.get_discounted_price(100), 75.0)

      @expectedFailure
      def test_patch_incorrect_class_attribute(self):
          with mock.patch.object(Pricer, 'PERCENTAGE', 1):
              pricer = Pricer()
              self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

      def test_patch_class_attribute(self):
          with mock.patch.object(Pricer, 'DISCOUNT', 1):
              pricer = Pricer()
              self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

          self.assertAlmostEqual(pricer.get_discounted_price(100), 80)
  ```

### Mocking class helpers

- The following example is the root of many problems regarding monkeypatching using Mock. It usually shows up on more mature codebases that start making use of frameworks and helpers at class definition. For example, imagine this hypothetical Field class helper:

  ```python
  class Field:
      def __init__(self, type_, default, value=None):
          self.type_ = type_
          self.default = default
          self._value = value

      @property
      def value(self):
          if self._value is None:
              return self.default
          else:
              return self._value
  ```

- Production code:

  ```python
  from helper import Field

  COUNTRIES = ('US', 'CN', 'JP', 'DE', 'ES', 'FR', 'NL')


  class CountryPricer:

      DISCOUNT = 0.8
      country = Field(type_="str", default=COUNTRIES[0])

      def get_discounted_price(self, price, country):
          if country == self.country.value:
              return price * self.DISCOUNT
          else:
              return price
  ```

- Code:

  ```python
  from unittest import TestCase, mock, expectedFailure
  from pricer import CountryPricer


  class TestCountryPrices(TestCase):

      def test_patch_constant(self):
          with mock.patch('pricer.COUNTRIES', ['GB']):
              pricer = CountryPricer()
              self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 80)  # FAIL!
  ```

- Code:

  ```python
  from unittest import TestCase, mock, expectedFailure
  # not importing `pricer`

  class TestCountryPrices(TestCase):

      def test_delayed_import(self):
          with mock.patch('pricer.COUNTRIES', ['GB']):
              from pricer import CountryPricer
              pricer = CountryPricer()
              self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 80)  # Still FAIL!
  ```

- Code:

  ```python
  from unittest import TestCase, mock, expectedFailure
  from pricer import CountryPricer


  class TestCountryPrices(TestCase):

      def test_patch_class_helper(self):
          with mock.patch('pricer.CountryPricer.country.default', 'GB'):
              pricer = CountryPricer()
              self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 80)

          pricer = CountryPricer()
          self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 100)
  ```

**[⬆ back to top](#list-of-contents)**

<br />

---

## References:

- https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832
