# Anti Patterns

</br>

## List of Contents:
### 1. [18 Common Python Anti-Patterns I Wish I Had Known Before](#content-1)



</br>

---

## Contents:

## [18 Common Python Anti-Patterns I Wish I Had Known Before](https://towardsdatascience.com/18-common-python-anti-patterns-i-wish-i-had-known-before-44d983805f0f) <span id="content-1"></span>

### 0-before to start, what’s an anti-pattern?
- Anti-patterns are certain patterns in software development that are considered bad programming practices.
- As opposed to design patterns which are common approaches to common problems that have been formalized and are generally considered a good development practice, anti-patterns are the opposite and are undesirable.
- Introducing anti-patterns happens for many reasons:
  - absence of code review
  - a willingness to try out “cool” stuff when simple things might do the trick
  - not using the right tools (code linters and formatters to follow PEP8 conventions, docstrings generators, IDEs that support auto-completion, to name a few)
  - or simply not knowing a better alternative, which is fine as long as you learn and grow
- Anti-patterns can be spread into one or many of these categories:
  - Correctness: Anti-patterns that will literally break your code or make it do the wrong things.
  - Maintainability: Anti-patterns that will make your code hard to maintain or extend.
  - Readability: Anti-patterns that will make your code hard to read or understand.
  - Performance: Anti-patterns that will unnecessarily slow your code down.
  - Security: Anti-patterns that will pose a security risk to your program.


### 1 — Using non-explicit variable names
- Your variable names should always be descriptive to provide a minimum context.
- Example:
  ```python
  # bad practice

  df = pd.read_csv("./customer_reviews.csv")
  x = df.groupby("country").agg({"satisfaction_score": "mean"})

  # good practice

  customer_data = pd.read_csv("./customer_reviews.csv")
  average_satisfaction_per_country = customer_data.groupby("country").agg({"satisfaction_score": "mean"})

  # bad practice

  x = data[["f1", "f2", "f3"]]
  y = data["target"]

  # good practice

  features = data[["f1", "f2", "f3"]]
  target = data["target"]
  ```
- TIP 👉: don’t be afraid to use long variable names to be descriptive.

### 2 — Ignoring comments
- Code should always be clear in what it’s doing and comments should clarify why you are doing it.
- When your code is self-explanatory, comments are not needed.

### 3 — Forgetting to update comments
- Comments that contradict the code are worse than no comments at all.


### 4 — Using CamelCase in function names
- This thing could happen if you are coming from another programming languages. So be aware
  ```python
  # bad practice
  def computeNetValue(price, tax):
      # ...

  # good practice
  def compute_net_value(price, tax):
      # ...
  ```

### 5 — Not iterating directly over the elements of an iterator
- You don’t necessarily need to iterate over the indices of the elements in an iterator if you don’t need them. 
- Example:
  ```python
  list_of_fruits = ["apple", "pear", "orange"]

  # bad practice

  for i in range(len(list_of_fruits)):
      fruit = list_of_fruits[i]
      process_fruit(fruit)
  		
  # good practice

  for fruit in list_of_fruits:
      process_fruit(fruit)
  ```

### 6 — Not using enumerate when you need the element and its index at the same time
- When you need to access an element and its index at the same time when iterating over an iterator, use enumerate.
- Example:
  ```python
  list_of_fruits = ["apple", "pear", "orange"]

  # bad practice 

  for i in range(len(list_of_fruits)):
      fruit = list_of_fruits[i]
      print(f"fruit number {i+1}: {fruit}")

  # good practice

  for i, fruit in enumerate(list_of_fruits):
      print(f"fruit number {i+1}: {fruit}")
  ```

### 7 — Not using zip to iterate over pairs of lists.
- `zip` is a useful built-in function that allows you to create a list of tuples from two iterators. the first element of each tuple comes from the first iterator, whereas the second element comes from the second iterator.
- Example:
  ```python
  list_of_letters = ["A", "B", "C"]
  list_of_ids = [1, 2, 3]

  # bad practice 

  for i in range(len(list_of_letters)):
      letter = list_of_letters[i]
      id_ = list_of_ids[i]
      process_letters(letter, id_)
  		
  # good practice

  # list(zip(list_of_letters, list_of_ids)) = [("A", 1), ("B", 2), ("C", 3)]

  for letter, id_ in zip(list_of_letters, list_of_ids):
      process_letters(letter, id_)
  ```

### 8 — Not using a context manager when reading or writing files
- Example:
  ```python
  d = {"foo": 1}

  # bad practice 

  f = open("./data.csv", "wb")
  f.write("some data")

  v = d["bar"] # KeyError
  # f.close() never executes which leads to memory issues

  f.close()

  # good practice

  with open("./data.csv", "wb") as f:
      f.write("some data")
      v = d["bar"]
  # python still executes f.close() even if the KeyError exception occurs
  ```

### 9 — Using in to check if an element is contained in a (large) list
- Example:
  ```python
  # bad practice
  list_of_letters = ["A", "B", "C", "A", "D", "B"]
  check = "A" in list_of_letters

  # good practice
  set_of_letters = {"A", "B", "C", "D"}
  check = "A" in set_of_letters
  ``` 

### 10 — Passing mutable default arguments to functions (i.e. an empty list)
- This means that if you use a mutable default argument (such as a list) and mutate it, you will and have mutated that object for all future calls to the function as well.
- Example:
  ```python
  # bad practice

  def append_to(element, to=[]):
      to.append(element)
      return to

  >>> my_list = append_to("a") 
  >>> print(my_list)
  >>> ["a"]

  >>> my_second_list = append_to("b") 
  >>> print(my_second_list)
  >>> ["a", "b"]

  # good practice 

  def append_to(element, to=None):
      if to is None:
          to = []
      to.append(element)
      return to
  ```
- To avoid this issue, you can set the default argument toto None.


### 11 — Returning different types in a single function
- Example:
  ```python
  # bad practice

  def get_code(username):
      if username != "ahmed":
          return "Medium2021"
      else:
          return None

  code = get_code("besbes")

  # good practice: raise an exception and catch it

  def get_code(username):
      if username != "ahmed":
          return "Medium2021"
      else:
          raise ValueError

  try:
      secret_code = get_code("besbes")
      print("The secret code is {}".format(secret_code))
  except ValueError:
      print("Wrong username.")
  ```

### 12 — Using while loops when simple for loops would do the trick
- Example:
  ```python
  # bad practice

  i = 0
  while i < 5:
      i += 1 
      some_processing(i) 
      ...

  # good practice

  for i in range(5):
      some_processing(i) 
      ...
  ```

### 13 — Using stacked and nested if statements
- Example:
  ```python
  user = "Ahmed"
  age = 30
  job = "data scientist"

  # bad practice

  if age > 30:
      if user == "Ahmed":
          if job == "data scientist":
              access = True
          else:
              access = False

  # good practice

  access = age > 30 and user == "ahmed" and job == "data scientist"
  ```

### 14 — Using global variables
- Avoid global variables like the plague.
- Example:
  ```python
  x = 0

  def complex_processing(i):
      global x
      x += 1
      return x

  >>> complex_processing(1)
  >>> x 
  1
  >>> complex_processing(1)
  >>> x
  2
  ```

### 15 — Not using get() to return default values from a dictionary
- When you use get, python checks if the specified key exists in the dictionary. If it does, then get() returns the value of that key. If the key doesn't exist, get() returns the value specified in the second argument.
- Example:
  ```python
  user_ids = {
      "John": 12,
      "Anna": 2,
      "Jack": 10
  }

  # bad practice

  name = "Paul"

  if name in user_ids:
      user_id = user_ids[name]
  else:
      user_id = None

  # good practice

  user_id = user_ids.get(name, None)
  ```

### 16 — Using try/except blocks that don’t handle exceptions meaningfully
- Using a try/except block and ignoring the exception by passing it (for instance) should be avoided.
- Example:
  ```python
  user_ids = {"John": 12, "Anna": 2, "Jack": 10}

  user = "Paul"
  # bad practice

  try:
      user_id = user_ids[user]
  except:
      pass

  # good practice

  try:
      user_id = user_ids[user]
  except KeyError:
      print("user id not found")
  ```

### 17 — proudly typing: from module import *
- Imports should always be specific. Importing * from a module is a very bad practice that pollutes the namespace.
- Example:
  ```python
  # bad practice 

  from math import *
  x = ceil(x)

  # good practice 

  from math import ceil   
  x = ceil(x) # we know where ceil comes from
  ```


### 18 —Over-engineering everything
- You don’t always need a class. Simple functions can be very useful.
- Essentially, a class is a way of grouping functions (as methods) and data (as properties) into a logical unit revolving around a certain kind of thing. If you don’t need that grouping, there’s no need to make a class.
- Example:
  ```python
  # bad practice

  class Rectangle:
      def __init__(self, height, width):
          self.height = height
          self.width = width
      
      def area(self):
          return self.height * self.width

  # good practice: a simple function is enough

  def area(height, width):
      return height * width
  ```


**[⬆ back to top](#list-of-contents)**

</br>

---

## References:
- https://towardsdatascience.com/18-common-python-anti-patterns-i-wish-i-had-known-before-44d983805f0f