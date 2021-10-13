# Python Concepts

<br />

## List of Contents:
### 1. [5 Pairs of Magic Methods in Python That You Should Know](#content-1)
### 2. [4 Ways To Level Up Your Python Code](#content-2)
### 3. [10 Advanced Python Concepts To Level Up Your Python Skills](#content-3)
### 4. [6 Alternatives to Classes in Python](#content-4)


<br />

---

## Contents:

## [5 Pairs of Magic Methods in Python That You Should Know](https://betterprogramming.pub/5-pairs-of-magic-methods-in-python-you-should-know-f98f0e5356d6) <span id="content-1"></span>


### 1. Instantiation: `__new__` and `__init__`
- Simple example:
  ```python
  class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
  ```
- In essence, the` __new__` method actually creates the instance object, which is passed to the `__init__` method to complete the initialization process.
- In other words, constructing a new instance object (a process known as instantiation) involves calling both `__new__` and `__init__` methods sequentially.
- Example:
  ```python
  >>> class Product:
  ...     def __new__(cls, *args):
  ...         new_product = object.__new__(cls)
  ...         print("Product __new__ gets called")
  ...         return new_product
  ... 
  ...     def __init__(self, name, price):
  ...         self.name = name
  ...         self.price = price
  ...         print("Product __init__ gets called")
  ... 
  >>> product = Product("Vacuum", 150.0)
  Product __new__ gets called
  Product __init__ gets called
  ```
  ```python
  from dataclasses import dataclass

  @dataclass
  class Person:
    name: str
    age: int

    __slots__ = ['name', 'age']

    def __new__(cls, *args):
      new_person = object.__new__(cls)
      print('Person __new__ gets called')
      return new_person

    def __init__(self, name, age):
      self.name = name
      self.age= age
      print('Person __init__ gets called')

  if __name__ == '__main__':
    sherlock = Person("Sherlock", 23)
    print(sherlock)
  ```

### 2. String Representation: `__repr__` and `__str__`
- The `__repr__` method should return a string that shows how the instance object can be created.
- Specifically, the string can be passed to eval() to re-construct the instance object.
- Example:
  ```python
  >>> product = Product("Vacuum", 150.0)
  >>> repr(product)
  "Product('Vacuum', 150.0)"
  >>> evaluated = eval(repr(product))
  >>> type(evaluated)
  <class '__main__.Product'>
  ```
- It should be noted that the `__str__` method is used by the print() function to display the instance-related information, as shown below.
- Although both methods should return strings, the `__repr__` method is usually intended for developers, so we want to show the instantiation information, while the `__str__` method is for regular users, so we want to show something more informational.


### 3. Iteration: `__iter__` and `__next__`
- Example:
  ```python
  for item in iterable:
      # Operations go here
  ```
- Under the hood, the iterable is converted to an iterator, which presents items from the iterable for each loop.
- Generally speaking, iterators are Python objects that can be used to render items to be iterated.
- The conversion is done by implementing the `__iter__` special method.
- In addition, retrieving the next item of the iterator involves the implementation of the `__next__` special method.
- Example:
  ```python
  >>> class Product:
  ...     def __init__(self, name, price):
  ...         self.name = name
  ...         self.price = price
  ... 
  ...     def __str__(self):
  ...         return f"Product: {self.name}, ${self.price:.2f}"
  ... 
  ...     def __iter__(self):
  ...         self._free_samples = [Product(self.name, 0) for _ in range(3)]
  ...         print("Iterator of the product is created.")
  ...         return self
  ... 
  ...     def __next__(self):
  ...         if self._free_samples:
  ...             return self._free_samples.pop()
  ...         else:
  ...             raise StopIteration("All free samples have been dispensed.")
  ... 
  >>> product = Product("Perfume", 5.0)
  >>> for i, sample in enumerate(product, 1):
  ...     print(f"Dispense the next sample #{i}: {sample}")
  ... 
  Iterator of the product is created.
  Dispense the next sample #1: Product: Perfume, $0.00
  Dispense the next sample #2: Product: Perfume, $0.00
  Dispense the next sample #3: Product: Perfume, $0.00
  ```
  ```python
  from dataclasses import dataclass
  from typing import List

  @dataclass
  class Person:
    name: str
    age: int
    _characters: List

    __slots__ = ['name', 'age', '_characters']

    def __new__(cls, *args):
      new_person = object.__new__(cls)
      print('Person __new__ gets called')
      return new_person

    def __init__(self, name, age):
      self.name = name
      self.age= age
      self._characters = None
      print('Person __init__ gets called')

    def __iter__(self):
      self._characters = [Person(name, 21) for name in ['Sherlock', 'John', 'Moriarty']]
      return self

    def __next__(self):
      if self._characters:
        return self._characters.pop()
      else:
        raise StopIteration("I've done and ready to move on!")

  if __name__ == '__main__':
    sherlock = Person("Sherlock", 23)
    print(sherlock)
    for i, name in enumerate(sherlock):
      print(name)
  ```


### 4. Context Manager: `__enter__` and `__exit__`
- Syntax:
  ```python
  with open('filename.txt') as file:
      # Your file operations go here
  ```
- So, in general, context managers are Python objects that manage shared resources, such as open and close, for us. Without them, we have to manage them manually, which can be error-prone.
- To implement such behavior with a custom class, our class needs to implement the `__enter__` and `__exit__` methods. The `__enter__` method sets up the context manager that prepares the needed resource for us to operate on, while the `__exit__` method is to clean up any used resources that should be released to make them available.
- Example:
  ```python
  >>> class Product:
  ...     def __init__(self, name, price):
  ...         self.name = name
  ...         self.price = price
  ... 
  ...     def __str__(self):
  ...         return f"Product: {self.name}, ${self.price:.2f}"
  ... 
  ...     def _move_to_center(self):
  ...         print(f"The product ({self}) occupies the center exhibit spot.")
  ... 
  ...     def _move_to_side(self):
  ...         print(f"Move {self} back.")
  ... 
  ...     def __enter__(self):
  ...         print("__enter__ is called")
  ...         self._move_to_center()
  ... 
  ...     def __exit__(self, exc_type, exc_val, exc_tb):
  ...         print("__exit__ is called")
  ...         self._move_to_side()
  ... 
  >>> product = Product("BMW Car", 50000)
  >>> with product:
  ...     print("It's a very good car.")
  ... 
  __enter__ is called
  The product (Product: BMW Car, $50000.00) occupies the center exhibit spot.
  It's a very good car.
  __exit__ is called
  Move Product: BMW Car, $50000.00 back.
  ```

### 5. Finer Attribute Access Control: `__getattr__` and `__setattr__`
- Specifically, the `__getattr__` method is called when attributes of an instance object are accessed, while the `__setattr__` method is called when we’re setting attributes of an instance object.
- Example:
  ```python
  >>> class Product:
  ...     def __init__(self, name):
  ...         self.name = name
  ... 
  ...     def __getattr__(self, item):
  ...         if item == "formatted_name":
  ...             print(f"__getattr__ is called for {item}")
  ...             formatted = self.name.capitalize()
  ...             setattr(self, "formatted_name", formatted)
  ...             return formatted
  ...         else:
  ...             raise AttributeError(f"no attribute of {item}")
  ... 
  ...     def __setattr__(self, key, value):
  ...         print(f"__setattr__ is called for {key!r}: {value!r}")
  ...         super().__setattr__(key, value)
  ... 
  >>> product = Product("taBLe")
  __setattr__ is called for 'name': 'taBLe'
  >>> product.name
  'taBLe'
  >>> product.formatted_name
  __getattr__ is called for formatted_name
  __setattr__ is called for 'formatted_name': 'Table'
  'Table'
  >>> product.formatted_name
  'Table'
  view raw
  ```
- The __setattr__ method is called every time we try to set an attribute of the object. To use it correctly, you have to use the superclass method by using super(). Otherwise, it will be running into an infinite recursion.
- As a side note, there’s another special method closely related to access control called __getattribute__, which is similar to __getattr__, but is called every time when an attribute is accessed. 
- In this regard, it’s similar to __setattr__ — likewise, you should use super() to implement the __getattribute__ method to avoid infinite recursion error.
- Example:
  ```python
  from dataclasses import dataclass
  from typing import List

  class Person:
    name: str
    age: int
    _characters: List

    def __new__(cls, *args):
      new_person = object.__new__(cls)
      print('Person __new__ gets called')
      return new_person

    def __init__(self, name, age):
      self.name = name
      self.age= age
      self._characters = None
      print('Person __init__ gets called')

    def __iter__(self):
      self._characters = [Person(name, 21) for name in ['Sherlock', 'John', 'Moriarty']]
      return self

    def __next__(self):
      if self._characters:
        return self._characters.pop()
      else:
        raise StopIteration("I've done and ready to move on!")

    def __enter__(self):
      print('__enter__is called')
    
    def __exit__(self, exc_type, exc_val, exc_tb):
      print('__exit__ is called')

    def __getattr__(self, item):
      if item == 'formatted_name':
        formatted = self.name.capitalize()
        setattr(self, 'formatted_name', formatted)
        return formatted
      else:
        raise AttributeError(f'No attribute of {item}')

    def __setattr__(self, key, value):
      super().__setattr__(key, value)

  if __name__ == '__main__':
    sherlock = Person("Sherlock", 23)
    print(sherlock)
    for i, name in enumerate(sherlock):
      print(name)

    with sherlock:
      print('Inside a context manager')

    print(sherlock.formatted_name)

  ```

**[⬆ back to top](#list-of-contents)**

<br />

---

## [4 Ways To Level Up Your Python Code](https://betterprogramming.pub/4-ways-to-level-up-your-python-code-f148a50efeea) <span id="content-2"></span>

### 1. Replace range(len()) With enumerate()
- Using the enumerate() function is a much more elegant and cleaner way.
- The enumerate function returns an enumerate object that stores each item’s index and value.
- Example:
  ```python
  # Define a collection, such as list:
  names = ['Nik', 'Jane', 'Katie', 'Jim', 'Luke']
  
  # Using the range(len(collection)) method, you'd write:
  for i in range(len(names)):
      print(i, names[i])
  
  # Using enumerate, you can define this by writing:
  for idx, name in enumerate(names):
      print(idx, name)
      
  # Both ways of doing this return:
  # 0 Nik
  # 1 Jane
  # 2 Katie
  # 3 Jim
  # 4 Luke
  ```
- As a bonus, if you wanted your enumerate object to begin somewhere other than 0, you could simply pass your starting value into the start= parameter.
  ```python
  # Define a collection, such as list:
  names = ['Nik', 'Jane', 'Katie', 'Jim', 'Luke']
  
  # Using enumerate, you can define this by writing:
  for idx, name in enumerate(names, start=1):
      print(idx, name)
      
  # This returns:
  # 1 Nik
  # 2 Jane
  # 3 Katie
  # 4 Jim
  # 5 Luke
  ```

### 2. Stop Using Square Brackets To Get Dictionary Items — Use .get()
- We have a dictionary like this:
  ```python
  
  nik = {
    'age':32,
    'gender':'male',
    'employed':True,
  }
  ```
- For example, attempting to access a non-existent value of 'location' will raise a KeyError:
- The method will simply return None in the event of a missing key and continue on its happy way!
- Example:
  ```python
  nik = {
    'age':32,
    'gender':'male',
    'employed':True,
  }
  
  print(nik.get('location'))
  
  # Returns:
  # None
  ```

### 3. Simplify Iterating Over Multiple Lists With Zip()
- The obvious way:
  ```python
  names = ['Nik', 'Jane', 'Melissa', 'Doug']
  ages = [32, 28, 37, 53]
  gender = ['Male', 'Female', 'Female', 'Male']
  
  # Old boring way:
  for_looped = []
  for i in range(len(names)):
      for_looped.append((names[i], ages[i], gender[i]))
  
  print(for_looped)
  
  # Returns:
  # [('Nik', 32, 'Male'), ('Jane', 28, 'Female'), ('Melissa', 37, 'Female'), ('Doug', 53, 'Male')]
  
  ```
- Note: The zip() function returns a zip object, but you can coerce it into different datatypes directly using, say, the list(), tuple(), or dict() functions.
- Using zip:
  ```python
  names = ['Nik', 'Jane', 'Melissa', 'Doug']
  ages = [32, 28, 37, 53]
  gender = ['Male', 'Female', 'Female', 'Male']
  
  # Zipping through lists with zip()
  zipped = zip(names, ages, gender)
  zipped_list = list(zipped)
  
  print(zipped_list)
  
  # Returns:
  # [('Nik', 32, 'Male'), ('Jane', 28, 'Female'), ('Melissa', 37, 'Female'), ('Doug', 53, 'Male')]
  ```
- Coerce zip object into dictionary. But you could only this with only two collections. Doing this with more than two collections will raise a ValueError:
  ```python
  names = ['Nik', 'Jane', 'Melissa', 'Doug']
  ages = [32, 28, 37, 53]
  gender = ['Male', 'Female', 'Female', 'Male']
  
  ages = dict(zip(names,ages))
  
  print(ages)
  
  # Returns
  # {'Nik': 32, 'Jane': 28, 'Melissa': 37, 'Doug': 53}
  ```

### 4. Use f-strings To Easily Print to the Console
- Example:
  ```python
  some_variable = "HELLO!"
  
  print(f"some_variable={some_variable}")
  
  # Returns
  # some_variable=HELLO!
  ```
- Another way:
  ```python
  
  some_variable = "HELLO!"
  
  print(f"{some_variable=}")
  
  # Returns
  # some_variable=HELLO!
  ```

**[⬆ back to top](#list-of-contents)**

<br />

---

## [10 Advanced Python Concepts To Level Up Your Python Skills](https://levelup.gitconnected.com/10-advance-python-concepts-to-level-up-your-python-skills-da3d6284ad53) <span id="content-3"></span>

### 1. Exception Handling
- An exception is a condition that occurs during the execution of the program and interrupts the execution.
- We use try and exceptblocks to handle exceptions in python. 
- To handle multiple exceptions at a time we use multiple except blocks.
- try blocks contain the code which needs to be executed. except blocks contain the code that executes if try fails to execute. 
- else block only execute when a try block is executed successfully. A finally block always executes, it is independent of other blocks.
- Example:
  ```python
  import sys
  try:
    f = open('myfile.txt') 
    s = f.readline()
    i = int(s.strip())
  except OSError as err:
    print("OS error: {0}".format(err))
  except ValueError:
    print("Could not convert data to an integer.")
  except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
  finally:
    print("Operation Successfully Done!!")
  (Example Taken From Official Python Docs)
  ```

### 2. Collections
- Collections in python are referred to as containers that are used to store the data.
- The five most used data structures in the collection module are:
  - Counter: It takes an iterable and returns a dictionary where the key is an element and value is the count it occurred in the iterable. 
    - Example:
      ```python
      from collections import Counter
      data = [1,1,1,1,2,3,4,3,3,5,6,7,7]
      count = Counter(data)
      print(count)
      ---------------------------------------------------
      Counter({1: 4, 3: 3, 7: 2, 2: 1, 4: 1, 5: 1, 6: 1})
      ```
  - namedtuple: nametuple is introduced to assign more meaning to each position of a tuple.
    - Example:
      ```python
      from collections import namedtuple
      Direction = namedtuple('Direction','N,S,E,W')
      dt = Direction(4,74,0,0)
      print(dt)
      ---------------------------------------------
      Direction(N=4, S=74, E=0, W=0)
      ```
  - OrderedDict: An OrderedDict is a kind of dict that remembers the order they are inserted in.
    - Example:
      ```python
      from collections import OrderedDict
      dictt = OrderedDict()
      dictt['a'] = 5
      dictt['d'] = 2
      dictt['c'] = 1
      dictt['b'] = 3
      print(dictt)
      --------------------------------------------------------
      OrderedDict([('a', 5), ('d', 2), ('c', 1), ('b', 3)])
      ```
  - defaultdict: A defaultdict will return a default value for the key that is not present in the dictionary rather than showing a key error.
    - Example:
      ```python
      from collections import defaultdict
      dictt = defaultdict(int)
      dictt['a'] = 2
      print(dictt['a'])  ## return the value
      print(dictt['b'])  ## returns the default value
      -------------------------------
      2
      0
      ```
  - deque: It is a double-ended queue in which elements can be added and removed from both sides.
  
### 3. itertools
- product(iterable,iterable): cartesian product of two iterables
- permutation(iterable): all possible ordering with no repeated elements
- combinations(iterable,n): all possible combinations with specified length with no repetition. here n is the size of the combination tuple.
- combinations_with_replacement(iterable,n): all possible combinations with specified length with repetition.
- accumlate(iterable) : returns accumulate the sum of elements of iterable.
- groupby(iterable,key=FUNC) : return an iterator with consecutive keys and groups from the iterable.

### 4. lambda
- It is also known as an anonymous function.
- It has no body and doesn’t require the def keyword for definition.
- A lambda function can have any number of arguments but only one expression in it. The expression evaluates and returned. It has no return statement.
- Example:
  ```python
  even_or_odd = lambda a: a%2==0
  numbers = [1,2,3,4,5]
  even = list(map(even_or_odd,numbers))
  print(even)
  ---------------------------------
  [False, True, False, True, False]
  ```

### 5. Decorators
- A decorator is a feature in python that adds some new functionality to existing code without explicitly modifying it.
- There are two types of decorators — function and class decorators.
- A decorators function has an @ before the function name.
- To understand the concept of decorators we first need to understand one thing— Functions in python are class objects. Unlike other objects, they can be defined inside a function, passed as an argument in other functions, and even return as a function.
- Example:
  ```python
  import functools
  def decorator(func):
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
          a,b = args
          print(a*b)
          result = func(*args,**kwargs)
          print(a/b)
          return result
      return wrapper
  
  @decorator
  def add(x,y):
      return x+y
  result = add(5,6)
  print(result)
  ```

### 6. Generators
- yield is a keyword in python that is used to return a value from a function without destroying its current state or reference to a local variable.
- Example:
  ```python
  -------------- Fibonacci Series Using Generators ------------
  def fibon(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a, b = b, a + b
  for x in fibon(10):
     print (x)
  ```

### 7. Threading and Multiprocessing
- Threading and multiprocessing both are used to run multiple scripts simultaneously at the same time. A process is an instance of the program, and a thread is an entity in a process.
- Threading is a technique where multiple threads run at the same time to execute different tasks.
- Multiprocessing is a technique in which multiple processes run on different CPUs at the same time.
- Differences between process and thread:
  ![Process vs thread](https://miro.medium.com/max/1400/1*x79qDXHAfyMSktsuJ7DHeA.png)
  
### 8. Dunder Methods
- Dunder methods or Magic methods are those that have two underscores __ before and after the method.
- When you try to multiply two numbers using * a sign then the internal __mul__ method is called.
- Example:
  ```python
  num =  5
  num*6
  >> 30
  num.__mul__(6)
  >>30
  ```
  
### 9. Logging
- Logging is a process of capturing the flow of code as it executes. Logging helps in debugging the code easily.
- In python, we have a library logging that helps us to write logs onto a file. There are five levels of logging:
  - Debug: Used for diagnosing the problem with detailed information.
  - Info: Confirmation of success.
  - Warning: when an unexpected situation occurs.
  - Error: Due to a more serious problem than a warning.
  - Critical: Critical error after which the program can’t run itself.

### 10. Context Managers
- Context Managers are a great tool in python that help in resource management.
- Example:
  ```python
  file = open('data.txt','w')
  try:
    file.write("Hello")
  except:
     file.close()
  ```

**[⬆ back to top](#list-of-contents)**

<br />

---

## [6 Alternatives to Classes in Python](https://betterprogramming.pub/6-alternatives-to-classes-in-python-6ecb7206377) <span id="content-4"></span>

### Plain Classes
- You should use type annotations
- Example:
  ```python
  from typing import Optional
  
  
  class Position:
      MIN_LATITUDE = -90
      MAX_LATITUDE = 90
      MIN_LONGITUDE = -180
      MAX_LONGITUDE = 180
  
      def __init__(
          self, longitude: float, latitude: float, address: Optional[str] = None
      ):
          self.longitude = longitude
          self.latitude = latitude
          self.address = address
  
      @property
      def latitude(self) -> float:
          """Getter for latitude."""
          return self._latitude
  
      @latitude.setter
      def latitude(self, latitude: float) -> None:
          """Setter for latitude."""
          if not (Position.MIN_LATITUDE <= latitude <= Position.MAX_LATITUDE):
              raise ValueError(f"latitude was {latitude}, but has to be in [-90, 90]")
          self._latitude = latitude
  
      @property
      def longitude(self) -> float:
          """Getter for longitude."""
          return self._longitude
  
      @longitude.setter
      def longitude(self, longitude: float) -> None:
          """Setter for longitude."""
          if not (Position.MIN_LONGITUDE <= longitude <= Position.MAX_LONGITUDE):
              raise ValueError(f"longitude was {longitude}, but has to be in [-180, 180]")
          self._longitude = longitude
  
  
  pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
  pos2 = Position(42.1238762, 9.1649964)
  
  
  def get_distance(p1: Position, p2: Position) -> float:
      pass
  ```

### 1. Tuples
- They have a very low memory overhead, so we can address the elements by index very quickly.
- The problem with tuples is that you have no names for member attributes. You have to remember what each index represents
- Tuples are mutable
- Example:
  ```python
  from typing import Tuple, Optional
  pos1 = (49.0127913, 8.4231381, "Parkstraße 17")
  pos2 = (42.1238762, 9.1649964, None)
  def get_distance(p1: Tuple[float, float, Optional[str]],
                   p2: Tuple[float, float, Optional[str]]) -> float:
      pass
  ```
- The annotation for get_distance looks messy. A human should be given the information that p1 represents a location — not that the location contains two floats and an optional string.

### 2. Dictionaries
- Dicts have a bigger memory overhead compared to tuples, as you have to store the names somewhere, but they are still OK
- Accessing elements by index is fast. Dicts are always mutable, but there is the third-party package frozendict to solve this.
- Example:
  ```python
  
  from typing import Any, Dict
  pos1 = {"longitude": 49.0127913,
          "latitude": 8.4231381,
          "address": "Parkstraße 17"}
  pos2 = {"longitude": 42.1238762,
          "latitude": 9.1649964,
          "address": None}
  def get_distance(p1: Dict[str, Any],
                   p2: Dict[str, Any]) -> float:
      pass
  ```

### 3. Named Tuples
- They are actually tuples, but they have a name and a constructor that accepts keyword arguments.
- Most people use the factory function collections.namedtuple to generate the named tuple class, but I prefer to inherit from typing.NamedTuple and use inheritance combined with type annotations
  ```python
  # Old style, before Python 3.7
  from collections import namedtuple
  attribute_names = ["longitude", "latitude", "address"]
  Position = namedtuple("Position", attribute_names, defaults=(None,))
  
  # Python 3.7 and later:
  from typing import NamedTuple
  
  class Position(NamedTuple):
      longitude: int
      latitude: int
      address: int
  
  # Both are used in the same way
  pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
  pos2 = Position(42.1238762, 9.1649964)
  
  def get_distance(p1: Position, p2: Position) -> float:
      pass
  ```
- NamedTuples solve the issue of the annotations becoming hard to read. They thus also fix the issue of editor support that I mentioned earlier.
- Interestingly, NamedTuples are not type-aware:
  ```python
  
  >>> from collections import namedtuple
  >>> Coordinates = namedtuple("Coordinates", ["x", "y"])
  >>> BMI = namedtuple("BMI", ["weight", "size"])
  >>> a = Coordinates(60, 170)
  >>> b = BMI(60, 170)
  >>> a
  Coordinates(x=60, y=170)
  >>> b
  BMI(weight=60, size=170)
  >>> a == b
  True
  ```

### 4. attrs
- attrs is a third-party library that reduces boilerplate code. Developers can use it by adding the @attrs.s decorator above the class. Attributes are assigned the attr.ib() function
  ```python
  from typing import Optional
  import attr
  
  
  @attr.s
  class Position:
      longitude: float = attr.ib()
      latitude: float = attr.ib()
      address: Optional[str] = attr.ib(default=None)
  
      @longitude.validator
      def check_long(self, attribute, v):
          if not (-180 <= v <= 180):
              raise ValueError(f"Longitude was {v}, but must be in [-180, +180]")
  
      @latitude.validator
      def check_lat(self, attribute, v):
          if not (-90 <= v <= 90):
              raise ValueError(f"Latitude was {v}, but must be in [-90, +90]")
  
  
  pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
  pos2 = Position(42.1238762, 9.1649964)
  
  
  def get_distance(p1: Position, p2: Position) -> float:
      pass
  ```

### 5. Dataclass
- They are similar to attrs, but in the standard library. It’s especially important to note that dataclasses are “just” normal classes that happen to have lots of data in them.
- In contrast to attrs, data classes use type annotations instead of the attr.ib() notation.
- You can easily make it immutable by changing the decorator to @dataclass(frozen=True) — just like with attrs.
- Example:
  ```python
  from typing import Optional
  from dataclasses import dataclass
  
  
  @dataclass
  class Position:
      longitude: float
      latitude: float
      address: Optional[str] = None
  
        
  pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
  pos2 = Position(42.1238762, 9.1649964, None)
  
  
  def get_distance(p1: Position, p2: Position) -> float:
      pass
  ```
- Using `__post__init__` for attribute validation:
  ```python
  def __post_init__(self):
      if not (-180 <= self.longitude <= 180):
          v = self.longitude
          raise ValueError(f"Longitude was {v}, but must be in [-180, +180]")
      if not (-90 <= self.latitude <= 90):
          v = self.latitude
          raise ValueError(f"Latitude was {v}, but must be in [-90, +90]")
  ```
- Example:
  ```python
  @dataclass
  class Position:
      longitude: float
      latitude: float
      address: Optional[str] = None
  
      @property
      def latitude(self) -> float:
          """Getter for latitude."""
          return self._latitude
  
      @latitude.setter
      def latitude(self, latitude: float) -> None:
          """Setter for latitude."""
          if not (-90 <= latitude <= 90):
              raise ValueError(f"latitude was {latitude}, but has to be in [-90, 90]")
          self._latitude = latitude
  
      @property
      def longitude(self) -> float:
          """Getter for longitude."""
          return self._longitude
  
      @longitude.setter
      def longitude(self, longitude: float) -> None:
          """Setter for longitude."""
          if not (-180 <= longitude <= 180):
              raise ValueError(f"longitude was {longitude}, but has to be in [-180, 180]")
          self._longitude = longitude
  ```

### 6. Pydantic
- Pydantic is a third-party library that focuses on data validation and settings management.
- Example:
  ```python
  
  from typing import Optional
  from pydantic import validator
  from pydantic.dataclasses import dataclass
  
  
  @dataclass(frozen=True)
  class Position:
      longitude: float
      latitude: float
      address: Optional[str] = None
  
      @validator("longitude")
      def longitude_value_range(cls, v):
          if not (-180 <= v <= 180):
              raise ValueError(f"Longitude was {v}, but must be in [-180, +180]")
          return v
  
      @validator("latitude")
      def latitude_value_range(cls, v):
          if not (-90 <= v <= 90):
              raise ValueError(f"Latitude was {v}, but must be in [-90, +90]")
          return v
  
  
  pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
  pos2 = Position(longitude=42.1238762, latitude=9.1649964)
  
  
  def get_distance(p1: Position, p2: Position) -> float:
      pass
  ```

### Mutability and Hashability
- Having the option to mark classes as frozen to make their objects immutable is pretty nice.
- Implementing `__hash__` for a mutable object is problematic because the hash might change when the object is changed. 
- This means if the object is in a dictionary, the dictionary would need to know that the hash of the object has changed and store it in a different location. 
- For this reason, both dataclasses and Pydantic prevent the hashing of mutable classes by default. They have unsafe_hash, though.

### Default String Representation
- If we printed pos1 from the examples above, here is what we would get. The linebreaks and alignments were added to keep things nice to read. The original results are on one line:
  ```text
  >>> print(pos1)
  Plain class   : <__main__.Position object at 0x7f1562750640>
  # 1 Tuples    : (49.0127913, 8.4231381, 'Parkstraße 17')
  # 2 Dicts     : {'longitude': 49.0127913,
                   'latitude': 8.4231381,
                   'address': 'Parkstraße 17'}
  # 3 NamedTuple: Position(longitude=49.0127913,
                           latitude=8.4231381,
                           address='Parkstraße 17')
  # 4 attrs     : Position(longitude=49.0127913,
                           latitude=8.4231381,
                           address='Parkstraße 17')
  # 5 dataclass : Position(longitude=49.0127913,
                           latitude=8.4231381,
                           address='Parkstraße 17')
  ```
  
### Data Validation
- For the following, I will attempt to create Position(1234, 567). So both the longitude and latitude are wrong. Here are the error messages this triggers:
  ```text
  # Plain Class
  ValueError: Longitude was 11111, but has to be in [-180, 180]
  # 4: attr
  ValueError: Longitude was 1234, but must be in [-180, +180]
  # 5: dataclasses
  (same as plain classes is possible)
  # 6: Pydantic
  pydantic.error_wrappers.ValidationError: 2 validation errors for Position
  longitude
    Longitude was 1234.0, but must be in [-180, +180] (type=value_error)
  latitude
    Latitude was 567.0, but must be in [-90, +90] (type=value_error)
  ```
- This is the point I want to make: Pydantic gives you all the errors in a very clear way. Plain classes and attrs just give you the first error.

### Serialize to JSON
- Example:
  ```python
  from pydantic import BaseModel
  
  
  class GitlabUser(BaseModel):
      id: int
      username: str
  
  
  class GitlabMr(BaseModel):
      id: int
      squash: bool
      web_url: str
      title: str
      author: GitlabUser
  
  
  mr = GitlabMr(
      id=1,
      squash=True,
      web_url="http://foo",
      title="title",
      author=GitlabUser(id=42, username="Joe"),
  )
  json_str = mr.json()
  print(json_str)
  ```
- Result:
  ```json
  {"id": 1, "squash": true, "web_url": "http://foo", "title": "title", "author": {"id": 42, "username": "Joe"}}
  ```

### Memory
- Using `getsize` to know the size
- The Pydantic base model has quite an overhead, but you always have to keep things in perspective.
- If memory becomes problematic, then you will not switch from Pydantic to dataclasses or attrs.

### So When Do I Use What?
- Dict when you don’t know ahead of time what will be added. Please note that you can mix all of the others with dict and vice versa. So if you know what a part of the data structure will look like, then use something different.
- NamedTuple when you need a quick way to group data and mutability is not needed. And when it’s OK for you to not be type-aware.
- Dataclasses when you need mutability, want to be type-aware, or want to have the possibility of inheriting from the created dataclass.
- Pydantic BaseModel when you need to deserialize data.

**[⬆ back to top](#list-of-contents)**

<br />

---

## References:
- https://betterprogramming.pub/5-pairs-of-magic-methods-in-python-you-should-know-f98f0e5356d6
- https://betterprogramming.pub/4-ways-to-level-up-your-python-code-f148a50efeea
- https://levelup.gitconnected.com/10-advance-python-concepts-to-level-up-your-python-skills-da3d6284ad53
- https://betterprogramming.pub/6-alternatives-to-classes-in-python-6ecb7206377