# Python Concepts

<br />

## List of Contents:
### 1. [5 Pairs of Magic Methods in Python That You Should Know](#content-1)
### 2. [4 Ways To Level Up Your Python Code](#content-2)
### 3. [10 Advanced Python Concepts To Level Up Your Python Skills](#content-3)
### 4. [6 Alternatives to Classes in Python](#content-4)
### 5. [How to Write Awesome Python Classes](#content-5)
### 6. [The Definitive Guide to Python import Statements](#content-6)
### 7. [Advanced Object Oriented Features of Python](#content-7)
### 8. [Supercharge Your Classes With Python super()](#content-8)
### 9. [Deep Dive into Python Mixins and Multiple Inheritance](#content-9)



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

## [How to Write Awesome Python Classes](https://towardsdatascience.com/how-to-write-awesome-python-classes-f2e1f05e51a9) <span id="content-1"></span>


### Magic Methods
- Magic methods are functions that belong to a class. They can be both instances and class methods.
- The probably most important thing is that magic methods are not meant to be called directly by you!
- So how are magic methods invoked? They are invoked from certain actions that you apply to your class or instance of your class.
- As a sneak peek, for example, calling str(YourClass()) would invoke the magic method `__str__` or YourClass() + YourClass() would invoke `__add__` if you’ve implemented it.
- In contrast to the built-in version, the example will offer some more functionality and more importantly create datetime ranges instead of numeric ranges.
  ```python
  from datetime import datetime, timedelta
  from typing import Iterable
  from math import ceil


  class DateTimeRange:
      def __init__(self, start: datetime, end_:datetime, step:timedelta = timedelta(seconds=1)):
          self._start = start
          self._end = end_
          self._step = step

      def __iter__(self) -> Iterable[datetime]:
          point = self._start
          while point < self._end:
              yield point
              point += self._step

      def __len__(self) -> int:
          return ceil((self._end - self._start) / self._step)

      def __contains__(self, item: datetime) -> bool:
          mod = divmod(item - self._start, self._step)
          return item >= self._start and item < self._end and mod[1] == timedelta(0)

      def __getitem__(self, item: int) -> datetime:
          n_steps = item if item >= 0 else len(self) + item
          return_value = self._start + n_steps * self._step
          if return_value not in self:
              raise IndexError()

          return return_value
    
      def __str__(self):
          return f"Datetime Range [{self._start}, {self._end}) with step {self._step}"

  # Usage
  my_range = DateTimeRange(datetime(2021,1,1), datetime(2021,12,1), timedelta(days=12))
  print(my_range)
  assert len(my_range) == len(list(my_range))
  my_range[-2] in my_range
  my_range[2] + timedelta(seconds=12) in my_range
  for r in my_range:
      do_something(r)
  ```
- Explanation of the above code:
  - The first one, and probably the best-known one is the __init__ method. As you certainly know, this method is mainly used to initialize your class's instance attributes.
  - The next one is the __iter__ method. This is probably the most important one as it generates all the elements that are part of our datetime range.
  - You can easily identify a generator function when seeing the yield keyword.
  - This allows you to consume one element at a time and work with it without requiring you to have every element in memory.
  - With __len__ you can find out the number of elements that are part of your range by calling len(my_range) .
  - With `__contains__` you can check if an element is part of your range using the built-in syntax element in my_range.
  - The sixth and last magic method that I have added is `__str__` . What this method does is allow you to convert an instance of your class to a string. This becomes very handy when calling print(my_range) as print has to transform an instance into a string and therefore uses the `__str__` method.


**[⬆ back to top](#list-of-contents)**

<br />

---

## [The Definitive Guide to Python import Statements](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#:~:text=root%20test%2F%20folder.-,What%20is%20an%20import%20%3F,made%20available%20to%20the%20importer.) <span id="content-6"></span>

### Summary / Key Points
- `import` statements search through the list of paths in `sys.path`
- `sys.path` always includes the path of the script invoked on the command line and is agnostic to the working directory on the command line.
- importing a package is conceptually the same as importing that package’s `__init__.py` file

### Basic Definitions
- module: any `*.py` file. Its name is the file name.
- built-in module: a “module” (written in C) that is compiled into the Python interpreter, and therefore does not have a *.py file.
- package: any folder containing a file named `__init__.py` in it. Its name is the name of the folder.
in Python 3.3 and above, any folder (even without a __init__.py file) is considered a package
- object: in Python, almost everything is an object - functions, classes, variables, etc.

### Example directory structure
- Example:
  ```text
  test/                      # root folder
      packA/                 # package packA
          subA/              # subpackage subA
              __init__.py
              sa1.py
              sa2.py
          __init__.py
          a1.py
          a2.py
      packB/                 # package packB (implicit namespace package)
          b1.py
          b2.py
      math.py
      random.py
      other.py
      start.py
  ```

### What is an `import`?
- When a module is imported, Python runs all of the code in the module file.
- When a package is imported, Python runs all of the code in the package’s __init__.py file, if such a file exists.
- All of the objects defined in the module or the package’s __init__.py file are made available to the importer.

### Basics of the Python `import` and `sys.path`
- According to Python documentation, here is how an import statement searches for the correct module or package to import:
  - When a module named spam is imported, the interpreter first searches for a built-in module with that name. 
  - If not found, it then searches for a file named spam.py in a list of directories given by the variable `sys.path`.
  - `sys.path` is initialized from these locations:
    - The directory containing the input script (or the current directory when no file is specified).
    - PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
    - The installation-dependent default.
  - After initialization, Python programs can modify sys.path.
  - The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path.
  - This means that scripts in that directory will be loaded instead of modules of the same name in the library directory.
- Technically, Python’s documentation is incomplete. The interpreter will not only look for a file (i.e., module) named spam.py, it will also look for a folder (i.e., package) named spam.
- Note that the Python interpreter first searches through the list of built-in modules, modules that are compiled directly into the Python interpreter.
- This list of built-in modules is installation-dependent and can be found in sys.builtin_module_names (Python 2 and 3). Some modules that are commonly built-in include sys, math, itertools, and time, among others.
- Unlike built-in modules which are first in the search path, the rest of the modules in Python’s standard library (not built-ins) come after the directory of the current script.
- For example, on my computer (Windows 10, Python 3.6), the math module is a built-in module, whereas the random module is not. Thus, import math in start.py will import the math module from the standard library, NOT my own math.py file in the same directory.
- However, import random in start.py will import my random.py file, NOT the random module from the standard library.
- Also, Python imports are case-sensitive. import Spam is not the same as import spam.
- The function pkgutil.iter_modules (Python 2 and 3) can be used to get a list of all importable modules from a given path:
  ```python
  import pkgutil
  search_path = ['.'] # set to None to see all modules importable from sys.path
  all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
  print(all_modules)
  ```
- To see what is in sys.path, run the following in the interpreter or as a script:
  ```python
  import sys
  print(sys.path)
  ```
- `sys.path`: A list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.
- As initialized upon program startup, the first item of this list, `path[0]`, is the directory containing the script that was used to invoke the Python interpreter.
- If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), `path[0]` is the empty string, which directs Python to search modules in the current directory first.
- Let’s recap the order in which Python searches for modules to import:
  - built-in modules from the Python Standard Library (e.g. `sys`, `math`)
  - modules or packages in a directory specified by `sys.path`:
    - If the Python interpreter is run interactively, `sys.path[0]` is the empty string ''. This tells Python to search the current working directory from which you launched the interpreter, i.e., the output of pwd on Unix systems.
    - If we run a script with python `<script>.py,` `sys.path[0]` is the path to `<script>.py`.
    - directories in the PYTHONPATH environment variable
    - default `sys.path` locations, including remaining Python Standard Library modules which are not built-in
- Note that when running a Python script, `sys.path` doesn’t care what your current “working directory” is. It only cares about the path to the script.
- For example, if my shell is currently at the `test/` folder and I run python `./packA/subA/subA1.py`, then `sys.path` includes `test/packA/subA/` but NOT `test/`.

### All about __init__.py
- An `__init__.py` file has 2 functions.
  - convert a folder of scripts into an importable package of modules (before Python 3.3)
  - run package initialization code
- In order to import a module or package from a directory that is not in the same directory as the script we are writing (or the directory from which we run the Python interactive interpreter), that module needs to be in a package.
- As defined above, any directory with a file named __init__.py is a Python package. 
- The first time that a package or one of its modules is imported, Python will execute the __init__.py file in the root folder of the package if the file exists.
- All objects and functions defined in __init__.py are considered part of the package namespace.
- Example:
  ```python
  # test/packA/a1.py
  def a1_func():
    print("running a1_func()")
  ```
  ```python
  # test/packA/__init__.py
  ## this import makes a1_func directly accessible from packA.a1_func
  from packA.a1 import a1_func

  def packA_func():
      print("running packA_func()")
  ```
  ```python
  # test/start.py
  import packA  # "import packA.a1" will work just the same

  packA.packA_func()
  packA.a1_func()
  packA.a1.a1_func()
  ```
- If `a1.py` calls `import a2` and we run python `a1.py`, then `test/packA/__init__.py` will NOT be called, even though it seems like `a2` is part of the `packA` package. This is because when Python runs a script (in this case `a1.py`), its containing folder is not considered a package.

### Using Objects from the Imported Module or Package
- There are 4 different syntaxes for writing import statements.
  - `import <package>`
  - `import <module>`
  - `from <package> import <module or subpackage or object>`
  - `from <module> import <object>`
- Let X be whatever name comes after import.
  - If X is the name of a module or package, then to use objects defined in X, you have to write `X.object`.
  - If X is a variable name, then it can be used directly.
  - If X is a function name, then it can be invoked with `X()`
- Optionally, as Y can be added after any import X statement: import X as Y. This renames X to Y within the script. Note that the name X itself is no longer valid. A common example is import numpy as np.

### Use dir() to examine the contents of an imported module
- Example:
  ```python
  >>> from packA.subA import sa1
  >>> dir(sa1)
  ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'helloWorld']
  ```
- Importing a package is conceptually equivalent to importing the package’s __init__.py file as a module. Indeed, this is what Python treats the package as:
  
### Absolute vs. Relative Import
- An absolute import uses the full path (starting from the project’s root folder) to the desired module to import.
- A relative import uses the relative path (starting from the path of the current module) to the desired module to import. There are two types of relative imports:
  - an explicit relative import follows the format from `.<module/package> import X`, where `<module/package>` is prefixed by dots . that indicate how many directories upwards to traverse. A single dot . corresponds to the current directory; two dots .. indicate one folder up; etc
- Absolute imports:
  ```python
  import other
  import packA.a2
  import packA.subA.sa1
  ```
- Relative imports:
  ```python
  import other
  from . import a2
  from .subA import sa1
  ```
- Note that relative imports are based on the name of the current module. Since the name of the main module is always “main”, modules intended for use as the main module of a Python application must always use absolute imports.

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Advanced Object Oriented Features of Python](https://uwpce-pythoncert.github.io/SystemDevelopment/advanced_oo.html) <span id="content-7"></span>

### Multiple Inheritance
- Pulling methods from more than one class
- Snippet:
  ```python
  class Combined(Super1, Super2, Super3):
      def __init__(self, something, something else):
          Super1.__init__(self, ......)
          Super2.__init__(self, ......)
          Super3.__init__(self, ......)
  ```

### The Diamond Problem
- Snippet:
  ```python
  class A(object):
      def do_your_stuff(self):
          print("doing A's stuff")

  class B(A):
      def do_your_stuff(self):
          A.do_your_stuff(self)
          print("doing B's stuff")

  class C(A):
      def do_your_stuff(self):
          A.do_your_stuff(self)
          print("doing C's stuff")

  class D(B,C):
      def do_your_stuff(self):
          B.do_your_stuff(self)
          C.do_your_stuff(self)
          print("doing D's stuff")
  ```
- Problem: <br />
  ![](https://uwpce-pythoncert.github.io/SystemDevelopment/_images/Diamond_inheritance.png)

### The Method Resolution Order
- super() can handle the MRO for you dynamically
- Getting the superclass:
  ```python
  class SafeVehicle(Vehicle):
      """
      Safe Vehicle subclass of Vehicle base class...
      """
      def __init__(self, position=0, velocity=0, icon='S'):
          Vehicle.__init__(self, position, velocity, icon)
  ```
- Another way doing the same thing as the above:
  ```python
  class SafeVehicle(Vehicle):
      """
      Safe Vehicle subclass of Vehicle base class
      """
      def __init__(self, position=0, velocity=0, icon='S'):
          super().__init__(position, velocity, icon)
  ```

### What does super() do?
- super returns a “proxy object” that delegates method calls.
- It’s not returning the object itself – but you can call methods on it.
- It runs through the method resolution order (MRO) to find the method you call.
- Snippet:
  ```python
  class D(C, B, A):
      def __init__(self):
        super().__init__()
  ```
- Below is the same thing as above:
  ```python
  class D(C, B, A):
      def __init__(self):
        C.__init__()
        B.__init__()
        A.__init__()
  ```
- In python3, you can usually call super() with no arguments:
  ```python
  class B(A):
      def a_method(self, *args, **kwargs)
          super().a_method(*args, **kwargs)
  ```

### Class Creation
- Snippet:
  ```python
  class Class():
      def __init__(self, arg1, arg2):
          self.arg1 = arg1
          self.arg2 = arg2
          .....
  ```
- The usual thing:
  - A new instance is created
  - `__init__` is called
  - The code in `__init__` is run to initialize the instance
- What if you need to do something before creation? Use `__new__`
  ```python
  class Class():
      def __new__(cls, arg1, arg2):
          some_code_here
          return cls(...)
          ...
  ```
- Flow:
  - `__new__` is called: it returns a new instance
  - The code in `__new__` is run to pre-initialize the instance
  - `__init__` is called
  - The code in `__init__` is run to initialize the instance
- Snippet:
  ```python
  class Class(superclass):
      def __new__(cls, arg1, arg2):
          some_code_here
          return superclass.__new__(cls)
          .....
  ```

### When to use `__new__`
- When would you need to use it:
  - Subclassing an immutable type:
    - It’s too late to change it once you get to `__init__`
  - When `__init__` is not called:
    - unpickling
    - copying

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Supercharge Your Classes With Python super()](https://realpython.com/python-super/) <span id="content-8"></span>

### An Overview of Python’s super() Function
- At a high level super() gives you access to methods in a superclass from the subclass that inherits from it.
- super() alone returns a temporary object of the superclass that then allows you to call that superclass’s methods.
- Calling the previously built methods with super() saves you from needing to rewrite those methods in your subclass, and allows you to swap out superclasses with minimal code changes.
- Inheritance is a concept in object-oriented programming in which a class derives (or inherits) attributes and behaviors from another class without needing to implement them again.

### super() in Single Inheritance
- Snippet:
  ```python
  class Rectangle:
      def __init__(self, length, width):
          self.length = length
          self.width = width

      def area(self):
          return self.length * self.width

      def perimeter(self):
          return 2 * self.length + 2 * self.width

  class Square:
      def __init__(self, length):
          self.length = length

      def area(self):
          return self.length * self.length

      def perimeter(self):
          return 4 * self.length
  ```
- Snippet using inherintance:
  ```python
  class Rectangle:
      def __init__(self, length, width):
          self.length = length
          self.width = width

      def area(self):
          return self.length * self.width

      def perimeter(self):
          return 2 * self.length + 2 * self.width

  # Here we declare that the Square class inherits from the Rectangle class
  class Square(Rectangle):
      def __init__(self, length):
          super().__init__(length, length)
  ```
- Because the Square and Rectangle `.__init__()` methods are so similar, you can simply call the superclass’s `.__init__()` method (Rectangle`.__init__()`) from that of Square by using super().

### What Can super() Do for You?
- Snippet:
  ```python
  class Square(Rectangle):
      def __init__(self, length):
          super().__init__(length, length)

  class Cube(Square):
      def surface_area(self):
          face_area = super().area()
          return face_area * 6

      def volume(self):
          face_area = super().area()
          return face_area * self.length
  ```
- Note that in our example above, super() alone won’t make the method calls for you: you have to call the method on the proxy object itself.

### A super() Deep Dive
- While the examples above (and below) call super() without any parameters, super() can also take two parameters: the first is the subclass, and the second parameter is an object that is an instance of that subclass.
- Snippet:
  ```python
  class Rectangle:
      def __init__(self, length, width):
          self.length = length
          self.width = width

      def area(self):
          return self.length * self.width

      def perimeter(self):
          return 2 * self.length + 2 * self.width

  class Square(Rectangle):
      def __init__(self, length):
          super(Square, self).__init__(length, length)
  ```
- In Python 3, the super(Square, self) call is equivalent to the parameterless super() call.
- The first parameter refers to the subclass Square, while the second parameter refers to a Square object which, in this case, is self. 
- Snippet:
  ```python
  class Cube(Square):
      def surface_area(self):
          face_area = super(Square, self).area()
          return face_area * 6

      def volume(self):
          face_area = super(Square, self).area()
          return face_area * self.length
  ```
- In this example, you are setting Square as the subclass argument to super(), instead of Cube. This causes super() to start searching for a matching method (in this case, .area()) at one level above Square in the instance hierarchy, in this case Rectangle.
- The parameterless call to super() is recommended and sufficient for most use cases, and needing to change the search hierarchy regularly could be indicative of a larger design issue.
- By including an instantiated object, super() returns a bound method: a method that is bound to the object, which gives the method the object’s context such as any instance attributes.
- If this parameter is not included, the method returned is just a function, unassociated with an object’s context.
- Technically, super() doesn’t return a method. It returns a proxy object. This is an object that delegates calls to the correct class methods without making an additional object in order to do so.

### super() in Multiple Inheritance
- In addition to single inheritance, Python supports multiple inheritance, in which a subclass can inherit from multiple superclasses that don’t necessarily inherit from each other (also known as sibling classes).
- Diagram: <br />
  ![](https://files.realpython.com/media/multiple_inheritance.22fc2c1ac608.png)
- Snippet:
  ```python
  class Triangle:
      def __init__(self, base, height):
          self.base = base
          self.height = height

      def area(self):
          return 0.5 * self.base * self.height

  class RightPyramid(Triangle, Square):
      def __init__(self, base, slant_height):
          self.base = base
          self.slant_height = slant_height

      def area(self):
          base_area = super().area()
          perimeter = super().perimeter()
          return 0.5 * perimeter * self.slant_height + base_area
  ```

### Method Resolution Order
- The method resolution order (or MRO) tells Python how to search for inherited methods.
- Every class has an .__mro__ attribute that allows us to inspect the order, so let’s do that:
  ```python
  >>> RightPyramid.__mro__
  (<class '__main__.RightPyramid'>, <class '__main__.Triangle'>, 
  <class '__main__.Square'>, <class '__main__.Rectangle'>, 
  <class 'object'>)
  ```
- This tells us that methods will be searched first in Rightpyramid, then in Triangle, then in Square, then Rectangle, and then, if nothing is found, in object, from which all classes originate.
- The problem here is that the interpreter is searching for .area() in Triangle before Square and Rectangle, and upon finding .area() in Triangle, Python calls it instead of the one you want. Because Triangle.area() expects there to be a .height and a .base attribute, Python throws an AttributeError.
- By changing the order:
  ```python
  class RightPyramid(Square, Triangle):
      def __init__(self, base, slant_height):
          self.base = base
          self.slant_height = slant_height
          super().__init__(self.base)

      def area(self):
          base_area = super().area()
          perimeter = super().perimeter()
          return 0.5 * perimeter * self.slant_height + base_area
  ```
- This causes issues with method resolution, because the first instance of .area() that is encountered in the MRO list will be called.
- When you’re using super() with multiple inheritance, it’s imperative to design your classes to cooperate. Part of this is ensuring that your methods are unique so that they get resolved in the MRO, by making sure method signatures are unique—whether by using method names or method parameters.
- Complete snippet:
  ```python
  class Rectangle:
      def __init__(self, length, width, **kwargs):
          self.length = length
          self.width = width
          super().__init__(**kwargs)

      def area(self):
          return self.length * self.width

      def perimeter(self):
          return 2 * self.length + 2 * self.width

  # Here we declare that the Square class inherits from 
  # the Rectangle class
  class Square(Rectangle):
      def __init__(self, length, **kwargs):
          super().__init__(length=length, width=length, **kwargs)

  class Cube(Square):
      def surface_area(self):
          face_area = super().area()
          return face_area * 6

      def volume(self):
          face_area = super().area()
          return face_area * self.length

  class Triangle:
      def __init__(self, base, height, **kwargs):
          self.base = base
          self.height = height
          super().__init__(**kwargs)

      def tri_area(self):
          return 0.5 * self.base * self.height

  class RightPyramid(Square, Triangle):
      def __init__(self, base, slant_height, **kwargs):
          self.base = base
          self.slant_height = slant_height
          kwargs["height"] = slant_height
          kwargs["length"] = base
          super().__init__(base=base, **kwargs)

      def area(self):
          base_area = super().area()
          perimeter = super().perimeter()
          return 0.5 * perimeter * self.slant_height + base_area

      def area_2(self):
          base_area = super().area()
          triangle_area = super().tri_area()
          return triangle_area * 4 + base_area
  ```

### Multiple Inheritance Alternatives
- If you see yourself beginning to use multiple inheritance and a complicated class hierarchy, it’s worth asking yourself if you can achieve code that is cleaner and easier to understand by using composition instead of inheritance.
- A mixin works as a kind of inheritance, but instead of defining an “is-a” relationship it may be more accurate to say that it defines an “includes-a” relationship. With a mix-in you can write a behavior that can be directly included in any number of other classes.
- Snippet mixin:
  ```python
  class Rectangle:
      def __init__(self, length, width):
          self.length = length
          self.width = width

      def area(self):
          return self.length * self.width

  class Square(Rectangle):
      def __init__(self, length):
          super().__init__(length, length)

  class VolumeMixin:
      def volume(self):
          return self.area() * self.height

  class Cube(VolumeMixin, Square):
      def __init__(self, length):
          super().__init__(length)
          self.height = length

      def face_area(self):
          return super().area()

      def surface_area(self):
          return super().area() * 6
  ```
- In this example, the code was reworked to include a mixin called VolumeMixin. The mixin is then used by Cube and gives Cube the ability to calculate its volume, which is shown below:


**[⬆ back to top](#list-of-contents)**

<br />

---

## [Deep Dive into Python Mixins and Multiple Inheritance](https://coderbook.com/@marcus/deep-dive-into-python-mixins-and-multiple-inheritance/) <span id="content-9"></span>

### Introduction
- Mixins in Python is just semantics. It’s not a “thing” by itself, its just classes and normal inheritance. But it’s when inheritance is done in a specific way. So in that manner, then you could say that Yes – Mixins are the “same thing” as multiple inheritance. But let’s explore it further than that.

### Mixins Cannot Be Intantiated By Themselves
- Mixins are small classes that focus on providing a small set of specific features that you can later combine with code that live in other classes
- Mixins are small classes that focus on providing a small set of specific features that you can later combine with code that live in other classes.
- Example:
  ```python
  class MetaMixin(object):
      """Mixin to enhance web view with meta data"""
      def get_meta_title(self) -> str:
          """Get meta title of page/view"""
          return str(self.get_object())
  ```
- As you can see, our code is calling the get_object() method. Where is that one defined? Not within our MetaMixin.
- If you would instantiate this class and call the get_meta_title method, an exception would be raised and the code wouldn’t be running. We expect some other code to define this method somewhere. We expect our Mixin to be “mixed in” with other classes and other code.
- Example of using mixin:
  ```python
  from .mixins import MetaMixin
  from .models import User

  class Foo(MetaMixin):
      def get_object(self):
          return User.get_user()
  ```
  ```python
  from .mixins import MetaMixin
  from .views import DetailView
  from .models import User

  class UserDetailView(MetaMixin, DetailView):
      model = User
  ```

### When to use Mixins in Python?
- In general, there are 2 cases where you would like to implement something like this:
  - You want to provide a lot of optional features for a class.
  - You want to use one particular feature in a lot of different classes.
- Instead of creating large classes that work with every combination of these features, or implementing them all in a single large class, we can instead compose our view classes with these features whenever they are needed.
- For example, imagine that we have a web view for an e-commerce store that represents a single Product. This type of view might be required for other types of database models as well such as a Customer, Category or Order. It, therefore, makes sense to create some kind of reusable code that we can use to automatically fetch the object from the database, maybe we can automatically expect there to be a slug or id url parameter that we could use to figure out which unique object we want to fetch.
- Example:
  ```python
  from .views import View
  from .models import Product, Category, Customer, Order

  class SingleObjectMixin(object):
      model = None
      def get_object(self, request):
          if self.model is None:
              raise Exception("Model must be set.")
          return self.model.get(id=request.kwargs.get("id")

  class ProductView(SingleObjectMixin, View):
      model = Product

  class CategoryView(SingleObjectMixin, View):
      model = Category

  class CustomerView(SingleObjectMixin, View):
      model = Customer

  class OrderView(SingleObjectMixin, View):
      model = Order
  ```
- Some of these views might also require authentication to be viewed, perhaps a user must be logged in to be able to see the details of an order. We can then imagine that we also have an AuthMixin that we could use to implement this behavior. We might, therefore, end up with the final code looking something like this:
- Example:
  ```python
  class ProductView(SingleObjectMixin, View):
      model = Product

  class CategoryView(SingleObjectMixin, View):
      model = Category

  class CustomerView(SingleObjectMixin, AuthMixin, View):
      model = Customer

  class OrderView(SingleObjectMixin, AuthMixin, View):
      model = Order
  ```
- As you can see, all of the new views that we have created inherit from the base View class, which contains the bulk of all logic or code required for our code to work. But all of them get unique behavior added to them in different ways using smaller Mixin classes that add specific, small sets of features to enhance the base class in different ways.

### What’s the Definition of a Python Mixin?
- Definitions of mixin:
  - Mixins are tools to create classes in compositional styles.
  - A mixin is meant to be “mixed in” to other pieces of code. It might run on its own, but it was not created with the intention to run on its own.
  - A mixin is a class that is implementing a small and specific set of features that is needed in many different classes.
  - There is no limit on how many mixins you can use to compose a new class. You can use 1 or 10, it’s all up to you as the developer to make that decision.
- Snippet:
  ```python
  class Foo(FirstMixin, SecondMixin, BaseClass):
      pass

  class Bar(BaseClass, SecondMixin, FirstMixin):
      pass
  ```
- The recommended and “logical” way to structure the order of your inheritance is to make the highest to lowest from left to right. So if you want FirstMixin to have the highest precedence, it should be defined as the first item, following the Foo class definition.

### Mixins vs Decorators in Python
- If you already have some experience with Python, you might notice that the use of Mixins has some similarities with the use of Python Decorators. Both are used to modify or add behavior that enhances or customizes another set of code.
- The main differences between Mixins and Decorators are:
  - Decorators wrap functionality around a piece of code.
  - Mixins add functionality to code using Inheritance.
- Mixins only work with Object-Oriented Programming and Classes
- Decorators cannot add new methods or new pieces of code.
- Generally, you could say that decorators are most commonly used to modify the behavior of existing code while Mixins are used to add new behaviors.
- For example, a decorator might be used to register a function to some collection and then returning the same function, or perhaps taking a function or class and then modifying it before returning it back again.
- A Mixin might be used to add a new set of methods to a class, instead of just modifying behavior it adds new blocks of code and new features to the existing class.
- Mixins are nicer to use for composing functionality of a new class. Theoretically, you could decorate a new class to compose it with functionality, but having a list of 5 decorators that wrap each other, is more confusing and difficult to understand than to use Mixins that compose the new behavior.


**[⬆ back to top](#list-of-contents)**

<br />

---

## References:
- https://betterprogramming.pub/5-pairs-of-magic-methods-in-python-you-should-know-f98f0e5356d6
- https://betterprogramming.pub/4-ways-to-level-up-your-python-code-f148a50efeea
- https://levelup.gitconnected.com/10-advance-python-concepts-to-level-up-your-python-skills-da3d6284ad53
- https://betterprogramming.pub/6-alternatives-to-classes-in-python-6ecb7206377
- https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#:~:text=root%20test%2F%20folder.-,What%20is%20an%20import%20%3F,made%20available%20to%20the%20importer.
- https://realpython.com/python-super/
- https://coderbook.com/@marcus/deep-dive-into-python-mixins-and-multiple-inheritance/