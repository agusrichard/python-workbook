# Python Concepts

</br>

## List of Contents:
### 1. [5 Pairs of Magic Methods in Python That You Should Know](#content-1)



</br>

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

</br>

---
## References:
- https://betterprogramming.pub/5-pairs-of-magic-methods-in-python-you-should-know-f98f0e5356d6