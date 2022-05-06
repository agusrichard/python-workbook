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

**[⬆ back to top](#list-of-contents)**

<br />

---

## References:

- https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832
