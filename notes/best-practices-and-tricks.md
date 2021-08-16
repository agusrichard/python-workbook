# Best Practices and Tricks in Python

## List of Contents:
### 1. [Python beyond beginner stage](#content-1)

</br>

---

## Contents:

## [Python beyond beginner stage](https://towardsdatascience.com/python-beyond-beginner-stage-good-practices-and-tools-75ddd55b445d) <span id="content-1"></span>

### Debugging
- Learning python debugger really pays off!
- We can use pdb
- Luckly if we're using vs code:
  - We can debugging multiprocessing and multithreading code.
  - Freedom to create a breakpoint while the code is running.

### Testing
- With experience you might realise that checking your program with different input scenarios or environmental conditions is important to avoid bugs breaking your software later on.
- Once your code starts interacting with other expensive and complex components you’ll want to test your code components (like functions and classes) in isolation. 
- For that you’ll need to temporarily remove other components and replace them with fixed output. This is called monkey-patching.
- In pytestyou can use monkeypatch and in unittest there is mock module.
- The other use cases for these testing frameworks are:
  - Checking all the test cases even if one fails. Counting the total number of errors.
  - Comparing two dictionaries, nested lists, floats (taking precision into account), and some other object types which can’t be simple compared using == .
  - Checking the arguments passed to a mock object and the number of times it was called along with the arguments for each call.
  - Asserting that an exception should be raised in a code block.
  - Running tests in parallel


### Development — use typing
- Example:
  ```python
  def get_marks(name: str) -> float:
    return random.rand() * 100
  ```
- How is it useful for us to use typing:
  - Reason 1: If we don't know the type returned by `get_marks` then we will have to make an assumption, it could be integer or float. Then let's say that we use `==` operator to assert the result. Then because of floating point precision there is a change that we can't assert the result correctly because of comparing different type.
  - Reason 2 Helps improve readability. The code reviewer will thank you. The people using your library will love you.
  - Reason 3 Type checkers. You can use libraries like mypy which uses type checking to determine whether certain operations are incompatible with the type of the object. For example, strings have .tolower() method but ints don’t. In large code bases it’s easier to run mypy than to run the program with all the test cases to figure out such a bug.
    - We can use typing in combination with FastAPI to have a good documentation of our API
    - Use pydantic to validate each value passed in its dataclass.

### Architecture — use dataclasses
- Instead of initialising your variables in `__init__` you can do the following:
  ```python
  from dataclasses import dataclass
  @dataclass
  class Food:
      name: str
      carbs_percent: int
      fiber_percent: int
      
      @property
      def net_carbs(self):
          return self.carbs_percent + self.fiber_percent
  Food("Apple", 40, fiber_percent=5).net_carbs 
  # returns 45
  ```
- There are a couple of frameworks which implement data classes. Along with the built-in dataclass library there is attrs and pydantic.
- One of the side-effects of using dataclasses is it forces you to type the variables which is a very good coding practice in Python.
- To specify the default value of the variables directly assign it in case the default value is immutable or use dataclasses.field to like following:
  ```python
  from dataclasses import field
  @dataclass
  class Food:
      name: str = ''
      subitems: list = field(default_factory=list)
  ```
  - If you directly assign subitems: list = [] any changes you do to one instance like Food().subitems.append(3) will change the value for ALL instances of Food.
  - For example, don’t do the following:
    ```python
    # USE DEFAULT FACTORY INSTEAD OF THE FOLLOWING
    @dataclass
    class Animal:
        name: str = ''
    @dataclass
    class Store:
        animal: Animal = Animal("dog")
    store1 = Store()
    store1.animal.name = "cat"
    store2 = Store()
    print(store2.animal.name) # prints "cat"
    ```
  - Instead do animal: `Animal = field(default_factory=lambda: Animal("dog"))`


### Architecture — use named tuples
- If you want to return multiple variables in python you usually do something like the following
  ```python
  def get_time_and_place() -> Tuple[datetime, str]:
    return datetime.now(), 'Combodia'
  ```
- There would be a problem when our function returned a quite long tuple. These problems can be solved by using either typing.NamedTuple or collections.namedtuple.
  ```python
  class TimeAndPlace(typing.NamedTuple):
      time: datetime
      place: str = 'Madagascar'
  def get_time_and_place() -> TimeAndPlace:
      output = TimeAndPlace(datetime.now())
      return output
  ```
  ```python
  mytime, myplace = TimeAndPlace(dattetime.now())
  TimeAndPlace(dattetime.now())[1] # returns Madagascar
  ```

### Architecture — use Enums
- Example:
  ```python
  from enum import Enum
  class Label(Enum):
      dog='dog'
      cat='cat'
  ```
- Enum is a data structure you use when you have distinct values for a particular variable.
- Label.cat.value returns the “cat” string back which can be used to serialise and save.


### Architecture — use pathlib
- The inbuilt pathlib implements an object-oriented approach of manipulating and validating file paths.

#### Iterate through a directory and reading file
- Using os:
  ```python
  import os
  for maybe_file in os.listdir(my_dir):
      if not os.path.isfile(maybe_file): continue
      with open(os.path.join(my_dir, file)) as f:
          print(f.read())
  ```
- Using pathlib:
  ```python
  from pathlib import Path
  for file in Path(my_dir).iterdir():
       if not file.is_file(): continue
       with file.open() as f:
           print(f.read())
  ```
- The key is Path object instantiated by passing a string like ./ which is an object representing the path. The object has methods and properties like is_file() , exists() , name , glob('*.jpeg')
- The biggest eye-catcher is the way a path is constructed using the / operator. Consider:
  ```python
  >>> os.path.join(new_dir, os.path.basename(file))
  /home/ubuntu/project/x.jpeg

  # vs

  >>> new_dir / file.name
  Path(/home/ubuntu/project/x.jpeg)
  ```

### Linting
- A linter helps you detect many types of errors without running the program.
- If you use any IDE like VS Code you can get the errors pinpointed with each save of the code.
- Detect misspelling
- If you’re using a class attribute which doesn’t exist, if you’re passing more arguments than the function expects or you’re passing an argument more than once.
- If you’ve type annotated, linters will catch all kind of type incompatibilities.
- It also creates warning if there are code smells like catching general Exception or unused variable in a code.
- It also suggests you to do refactoring and other best practices recommended in PEP and other places.
- I recommend using pylint and mypy simultaneously which can be done in VS code by setting the following flags in VS code settings (JSON)
  ```json
  "python.linting.mypyEnabled": true,
  "python.linting.pylintEnabled": true,
  ```


### Readability — styling and formatting
- Great libraries have docstrings for each function, class, class methods and module. I recommend google-style docstrings
- Code layout based on PEP8
- Use a combination of manual formatting and auto-formatter like yapf or autopep8 (there are others you may try).

### Conclusion
- Tools for debugging: pdb, vs code python extension and ipython magic commands
- Include these on code designs: dataclasses, enum, pathlib, namedtuples
- Testing frameworks: pytest and unittest
- Linter: mypy, pylint, pylance
- Follow PEP8 and docstring guide


**[⬆ back to top](#list-of-contents)**

</br>

---
## References:
- https://towardsdatascience.com/python-beyond-beginner-stage-good-practices-and-tools-75ddd55b445d