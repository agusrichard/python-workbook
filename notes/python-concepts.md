# Python Concepts

<br />

## List of Contents:
### 1. [5 Pairs of Magic Methods in Python That You Should Know](#content-1)
### 2. [4 Ways To Level Up Your Python Code](#content-2)
### 3. [10 Advanced Python Concepts To Level Up Your Python Skills](#content-3)


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

## References:
- https://betterprogramming.pub/5-pairs-of-magic-methods-in-python-you-should-know-f98f0e5356d6
- https://betterprogramming.pub/4-ways-to-level-up-your-python-code-f148a50efeea
- https://levelup.gitconnected.com/10-advance-python-concepts-to-level-up-your-python-skills-da3d6284ad53