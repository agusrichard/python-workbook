# Python Clean Code

<br />

## List of Contents:

### 1. [Python Clean Code: 6 Best Practices to Make Your Python Functions More Readable](#content-1)

### 2. [Clean Code in Python](#content-2)

### 3. [Clean Code Python](#content-3)

### 4. [Python beyond beginner stage](#content-4)

### 5. [Advanced Python: Consider These 10 Elements When You Define Python Functions](#content-5)

### 6. [How To Write Clean Code in Python](#content-6)

### 7. [Best Practices To Follow While Creating Classes In Python](#content-7)

### 8. [11 Refactoring Patterns To Elevate Your Python Code](#content-8)

### 9. [Python Refactoring Tips to Write Code in Pythonic Way](#content-9)

### 10. [12 Of My Favorite Python Practices For Better Functions](#content-10)

### 11. [Write Clean Python Code Using Pipes](#content-11)

### 12. [Python: Production-Level Coding Practices](#content-12)

### 13. [Python Code Quality: Tools & Best Practices](#content-13)

<br />

---

## Contents:

## [Python Clean Code: 6 Best Practices to Make Your Python Functions More Readable](https://towardsdatascience.com/python-clean-code-6-best-practices-to-make-your-python-functions-more-readable-7ea4c6171d60) <span id="content-1"></span>

### Motivation

- You want your Python function to:
  - be small
  - do one thing
  - contain code with the same level of abstraction
  - have fewer than 4 arguments
  - have no duplication
  - use descriptive names

### Get Started

- Look at this mouthful code: <br />

  ```python
  import xml.etree.ElementTree as ET
  import zipfile
  from os import listdir
  from os.path import isfile, join

  import gdown


  def main():

      load_data(
          url="https://drive.google.com/uc?id=1jI1cmxqnwsmC-vbl8dNY6b4aNBtBbKy3",
          output="Twitter.zip",
          path_train="Data/train/en",
          path_test="Data/test/en",
      )


  def load_data(url: str, output: str, path_train: str, path_test: str):

      # Download data from Google Drive
      output = "Twitter.zip"
      gdown.download(url, output, quiet=False)

      # Unzip data
      with zipfile.ZipFile(output, "r") as zip_ref:
          zip_ref.extractall(".")

      # Get train, test data files
      tweets_train_files = [
          file
          for file in listdir(path_train)
          if isfile(join(path_train, file)) and file != "truth.txt"
      ]
      tweets_test_files = [
          file
          for file in listdir(path_test)
          if isfile(join(path_test, file)) and file != "truth.txt"
      ]

      # Extract texts from each file
      t_train = []
      for file in tweets_train_files:
          train_doc_1 = [r.text for r in ET.parse(join(path_train, file)).getroot()[0]]
          t_train.append(" ".join(t for t in train_doc_1))

      t_test = []
      for file in tweets_test_files:
          test_doc_1 = [r.text for r in ET.parse(join(path_test, file)).getroot()[0]]
          t_test.append(" ".join(t for t in test_doc_1))

      return t_train, t_test


  if __name__ == "__main__":
      main()
  ```

- What's wrong with this mouthful code:
  - Awfully long
  - Tries to do multiple things
  - The code within the function is at multiple levels of abstractions.
  - The function has more than 3 arguments
  - There are multiple duplications
  - Function’s name is not descriptive

### Small

- A function should be small because it is easier to know what the function does.
- How small is small? There should rarely be more than 20 lines of code in one function.
- This indent level should not be greater than one or two
- Refactored: <br />

  ```python
  import zipfile

  def unzip_data(output: str):

      with zipfile.ZipFile(output, 'r') as zip_ref:
          zip_ref.extractall('.')
  ```

### Do One Task

- A function should complete only one task, not multiple tasks.
- Refactored: <br />

  ```python
  download_zip_data_from_google_drive(url, output_path)

  unzip_data(output_path)

  tweet_train, tweet_test = get_train_test_docs(path_train, path_test)
  ```

- Each function should only do one thing

### One Level of Abstraction

- The level of abstraction is the amount of complexity by which a system is viewed or programmed. The higher the level, the less detail. The lower the level, the more detail. — PCMag
- Before: <br />

  ```python
  from typing import List

  def extract_texts_from_multiple_files(path_to_file: str, files: list) -> List[str]:

      all_docs = []
      for file in files:
          list_of_text_in_one_file =[r.text for r in ET.parse(join(path_to_file, file_name)).getroot()[0]]
          text_in_one_file_as_string = ' '.join(t for t in list_of_text_in_one_file)
          all_docs.append(text_in_one_file_as_string)

      return all_docs
  ```

- After being refactored: <br />

  ```python
  from typing import List

  def extract_texts_from_multiple_files(path_to_file: str, files: list) -> List[str]:

      all_docs = []
      for file in files:
          text_in_one_file = extract_texts_from_each_file(path_to_file, file)
          all_docs.append(text_in_one_file)

      return all_docs

  def extract_texts_from_each_file(path_to_file: str, file_name: list) -> str:

      list_of_text_in_one_file =[r.text for r in ET.parse(join(path_to_file, file_name)).getroot()[0]]
      text_in_one_file_as_string = ' '.join(t for t in list_of_text_in_one_file)

      return text_in_one_file_as_string
  ```

### Duplication

- This code contains duplication: <br />

  ```python
  t_train = []
  for file in tweets_train_files:
      train_doc_1 =[r.text for r in ET.parse(join(path_train, file)).getroot()[0]]
      t_train.append(' '.join(t for t in train_doc_1))


  t_test = []
  for file in tweets_test_files:
      test_doc_1 =[r.text for r in ET.parse(join(path_test, file)).getroot()[0]]
      t_test.append(' '.join(t for t in test_doc_1))
  ```

- Refactored: <br />

  ```python
  from typing import Tuple, List

  def get_train_test_docs(path_train: str, path_test: str) -> Tuple[list, list]:
      tweets_train_files = get_files(path_train)
      tweets_test_files = get_files(path_test)

      t_train = extract_texts_from_multiple_files(path_train, tweets_train_files)
      t_test  = extract_texts_from_multiple_files(path_test, tweets_test_files)
      return t_train, t_test

  def extract_texts_from_multiple_files(path_to_file: str, files: list) -> List[str]:

      all_docs = []
      for file in files:
          text_in_one_file = extract_texts_from_each_file(path_to_file, file)
          all_docs.append(text_in_one_file)

      return all_docs
  ```

### Descriptive Names

- A long descriptive name is better than a short enigmatic name. A long descriptive name is better than a long descriptive comment. — Clean Code by Robert C. Martin
- Don’t be afraid to write long names. It is better to write long names rather than write vague names.
- If you try to shorten your code by writing something like get_texts , it would be difficult for others to understand exactly what this function does without looking at the source code.
- If the descriptive name of a function is too long such as download*file_from* Google_drive_and_extract_text_from_that_file . It is a good sign that your function is doing multiple things and you should split it into smaller functions.
- Variable name has to tell us about what it is and function name has to tell us about what it does

### Have Fewer than 4 Arguments

- A function should not have more than 3 arguments since it is a sign that the function is performing multiple tasks.
- If a function has more than 3 arguments, consider turning it into a class.
- One way to cluster our functions is by using class. This is how it's done: <br />

  ```python
  import xml.etree.ElementTree as ET
  import zipfile
  from os import listdir
  from os.path import isfile, join
  from typing import List, Tuple

  import gdown


  def main():

      url = "https://drive.google.com/uc?id=1jI1cmxqnwsmC-vbl8dNY6b4aNBtBbKy3"
      output_path = "Twitter.zip"
      path_train = "Data/train/en"
      path_test = "Data/test/en"

      data_getter = DataGetter(url, output_path, path_train, path_test)

      tweet_train, tweet_test = data_getter.get_train_test_docs()


  class DataGetter:
      def __init__(self, url: str, output_path: str, path_train: str, path_test: str):
          self.url = url
          self.output_path = output_path
          self.path_train = path_train
          self.path_test = path_test
          self.download_zip_data_from_google_drive()
          self.unzip_data()

      def download_zip_data_from_google_drive(self):

          gdown.download(self.url, self.output_path, quiet=False)

      def unzip_data(self):

          with zipfile.ZipFile(self.output_path, "r") as zip_ref:
              zip_ref.extractall(".")

      def get_train_test_docs(self) -> Tuple[list, list]:

          tweets_train_files = self.get_files(self.path_train)
          tweets_test_files = self.get_files(self.path_test)

          t_train = self.extract_texts_from_multiple_files(
              self.path_train, tweets_train_files
          )
          t_test = self.extract_texts_from_multiple_files(
              self.path_test, tweets_test_files
          )
          return t_train, t_test

      @staticmethod
      def get_files(path: str) -> List[str]:

          return [
              file
              for file in listdir(path)
              if isfile(join(path, file)) and file != "truth.txt"
          ]

      def extract_texts_from_multiple_files(
          self, path_to_file: str, files: list
      ) -> List[str]:

          all_docs = []
          for file in files:
              text_in_one_file = self.extract_texts_from_each_file(path_to_file, file)
              all_docs.append(text_in_one_file)

          return all_docs

      @staticmethod
      def extract_texts_from_each_file(path_to_file: str, file_name: list) -> str:

          list_of_text_in_one_file = [
              r.text for r in ET.parse(join(path_to_file, file_name)).getroot()[0]
          ]
          text_in_one_file_as_string = " ".join(t for t in list_of_text_in_one_file)

          return text_in_one_file_as_string


  if __name__ == "__main__":
      main()
  ```

### How do I write a function like this?

- Don’t try to be perfect when starting to write code. Start with writing down complicated code that matches your thoughts.
- Then as your code grows, ask yourself whether your function violates any of the practices mentioned above. If yes, refactor it. Test it. Then move on to the next function.

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Clean Code in Python](https://blog.devgenius.io/clean-code-in-python-8251eea292fa) <span id="content-2"></span>

### Introduction

- Clean code is a set of principles that seeks code to be:
  - Readable
  - Maintainable
  - Extendable
- The philosophy of Python aims to make the code “Pythonic”.

### The Python Zen

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren’t special enough to break the rules. Although practicality beats purity.
- Errors should never pass silently. Unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one — and preferably only one — obvious way to do it. Although that way may not be obvious at first unless you’re Dutch.
- Now is better than never. Although never is often better than _right_ now.
- If the implementation is hard to explain, it’s a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea — let’s do more of those!

### How to write clean code:

- PEP8 is a proposal for a style guide for Python code, it is optional, however it makes it easier to write better code, improving readability and quality.
- DRY (Don’t Repeat Yourself)
- KISS (Keep it simple stupid). The KISS principle intends to make code development as simple as possible.
- Any fool can write code that a computer can understand. Good programmers write code that humans can understand. — Martin Fowler

### What can we do?

- To write Pythonic code, we must know the features provided by the proper language, functionalities that allow us to easily understand and improve the readability as well.
- Use decorators: <br />

  ```python
  def operations(function):
    def wrapper(*args, **kwargs):
      try:
        print("Numbers:", *args)
        response = function(*args, **kwargs)
        print("Result:", response)
        return response
      except Exception as err:
        print(err)

    return wrapper

  @operations
  def subtraction(num_a, num_b):
    return num_a - num_b

  @operations
  def division(num_a, num_b):
    return num_a / num_b

  subtraction(5, 2)
  division(5, 2)
  ```

- Context managers: <br />

  ```python
  # Read a File

  file = open("path_file", mode="r")
  print(file.read())
  file.close()

  # Using context managers

  with open("path_file", mode="r") as file:
    print(file.read())
  ```

- Dunder Methods: <br />

  ```python
  class User:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def __repr__(self):
        return f'User: {self.name}'

    def __gt__(self, other_user):
        if self.age > other_user.age:
          print(f"{self.name} is older than {other_user.name}")
        else:
          print(f"{self.name} is younger than {other_user.name}")

  esteban = User("Esteban", 26)
  cristian = User("Cristian", 24)

  print(esteban)
  # Output: User: Esteban

  esteban > cristian
  # Output: Esteban is older than Cristian
  ```

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Clean Code Python](https://github.com/zedr/clean-code-python/blob/master/README.md) <span id="content-3"></span>

> Thank you to the author for writing such an awesome summary

### Introduction

- It's a guide to producing readable, reusable, and refactorable software in Python.
- Not every principle herein has to be strictly followed, and even fewer will be universally agreed upon. These are guidelines and nothing more, but they are ones codified over many years of collective experience by the authors of Clean Code.

### Variables

- Use meaningful and pronounceable variable names <br />

  ```python
  # Bad
  import datetime


  ymdstr = datetime.date.today().strftime("%y-%m-%d")
  ```

  ```python
  # Good
  import datetime


  current_date: str = datetime.date.today().strftime("%y-%m-%d")
  ```

- Use the same vocabulary for the same type of variable <br />

  ```python
  # Bad
  def get_user_info(): pass
  def get_client_data(): pass
  def get_customer_record(): pass
  ```

  ```python
  # Good
  def get_user_info(): pass
  def get_user_data(): pass
  def get_user_record(): pass
  ```

  ```python
  from typing import Union, Dict, Text

  class Record:
      pass


  class User:
      info : str

      @property
      def data(self) -> Dict[Text, Text]:
          return {}

      def get_record(self) -> Union[Record, None]:
          return Record()
  ```

- Use searchable names

  - By not naming variables that end up being meaningful for understanding our program, we hurt our readers.
  - Example: <br />

  ```python
  # Bad
  import time


  # What is the number 86400 for again?
  time.sleep(86400)
  ```

  ```python
  # Good
  import time


  # Declare them in the global namespace for the module.
  SECONDS_IN_A_DAY = 60 * 60 * 24
  time.sleep(SECONDS_IN_A_DAY)
  ```

- Use explanatory variables <br />

  ```python
  # Bad
  import re


  address = "One Infinite Loop, Cupertino 95014"
  city_zip_code_regex = r"^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$"

  matches = re.match(city_zip_code_regex, address)
  if matches:
      print(f"{matches[1]}: {matches[2]}")  # bad because we don't know what matches[1] and matches[2] stand for just by directly looking at them
  ```

  ```python
  # Not bad
  import re


  address = "One Infinite Loop, Cupertino 95014"
  city_zip_code_regex = r"^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$"
  matches = re.match(city_zip_code_regex, address)

  if matches:
      city, zip_code = matches.groups() # we increased the dependency to re, by using this second function
      print(f"{city}: {zip_code}")
  ```

  ```python
  # Good
  import re


  address = "One Infinite Loop, Cupertino 95014"
  city_zip_code_regex = r"^[^,\\]+[,\\\s]+(?P<city>.+?)\s*(?P<zip_code>\d{5})?$"

  matches = re.match(city_zip_code_regex, address)
  if matches:
      print(f"{matches['city']}, {matches['zip_code']}")
  ```

- Avoid Mental Mapping

  - Don’t force the reader of your code to translate what the variable means. Explicit is better than implicit. <br />
  - Example:

  ```python
  # Bad
  seq = ("Austin", "New York", "San Francisco") # we don't know what seq for

  for item in seq:
      #do_stuff()
      #do_some_other_stuff()

      # Wait, what's `item` again?
      print(item)
  ```

  ```python
  # Good
  locations = ("Austin", "New York", "San Francisco")

  for location in locations:
      #do_stuff()
      #do_some_other_stuff()
      # ...
      print(location)
  ```

- Don't add unneeded context
  - If your class/object name tells you something, don't repeat that in your variable name. <br />
  ```python
  # Bad
  class Car:
    car_make: str
    car_model: str
    car_color: str
  ```
  ```python
  # Good
  class Car:
    make: str
    model: str
    color: str
  ```
- Use default arguments instead of short circuiting or conditionals <br />

  ```python
  # Tricky
  import hashlib


  def create_micro_brewery(name):
      name = "Hipster Brew Co." if name is None else name
      slug = hashlib.sha1(name.encode()).hexdigest()
      # etc.
  ```

  ```python
  # Good
  from typing import Text
  import hashlib


  def create_micro_brewery(name: Text = "Hipster Brew Co."):
      slug = hashlib.sha1(name.encode()).hexdigest()
      # etc.
  ```

### Functions

- Function arguments (2 or fewer ideally)

  - Limiting the amount of function parameters is incredibly important because it makes testing your function easier.
  - Zero arguments is the ideal case. One or two arguments is ok, and three should be avoided.

  ```python
  # Bad
  def create_menu(title, body, button_text, cancellable):
      pass
  ```

  ```python
  # Java-esque
  class Menu:
      def __init__(self, config: dict):
          self.title = config["title"]
          self.body = config["body"]
          # ...

  menu = Menu(
      {
          "title": "My Menu",
          "body": "Something about my menu",
          "button_text": "OK",
          "cancellable": False
      }
  )
  ```

  ```python
  # Also
  from typing import Text


  class MenuConfig:
      """A configuration for the Menu.

      Attributes:
          title: The title of the Menu.
          body: The body of the Menu.
          button_text: The text for the button label.
          cancellable: Can it be cancelled?
      """
      title: Text
      body: Text
      button_text: Text
      cancellable: bool = False


  def create_menu(config: MenuConfig) -> None:
      title = config.title
      body = config.body
      # ...


  config = MenuConfig()
  config.title = "My delicious menu"
  config.body = "A description of the various items on the menu"
  config.button_text = "Order now!"
  # The instance attribute overrides the default class attribute.
  config.cancellable = True

  create_menu(config)
  ```

  ```python
  # Fancy
  from typing import NamedTuple


  class MenuConfig(NamedTuple):
      """A configuration for the Menu.

      Attributes:
          title: The title of the Menu.
          body: The body of the Menu.
          button_text: The text for the button label.
          cancellable: Can it be cancelled?
      """
      title: str
      body: str
      button_text: str
      cancellable: bool = False


  def create_menu(config: MenuConfig):
      title, body, button_text, cancellable = config
      # ...


  create_menu(
      MenuConfig(
          title="My delicious menu",
          body="A description of the various items on the menu",
          button_text="Order now!"
      )
  )
  ```

  ```python
  # Even fancier
  from typing import Text
  from dataclasses import astuple, dataclass


  @dataclass
  class MenuConfig:
      """A configuration for the Menu.

      Attributes:
          title: The title of the Menu.
          body: The body of the Menu.
          button_text: The text for the button label.
          cancellable: Can it be cancelled?
      """
      title: Text
      body: Text
      button_text: Text
      cancellable: bool = False

  def create_menu(config: MenuConfig):
      title, body, button_text, cancellable = astuple(config)
      # ...


  create_menu(
      MenuConfig(
          title="My delicious menu",
          body="A description of the various items on the menu",
          button_text="Order now!"
      )
  )
  ```

  ```python
  from typing import TypedDict, Text


  class MenuConfig(TypedDict):
      """A configuration for the Menu.

      Attributes:
          title: The title of the Menu.
          body: The body of the Menu.
          button_text: The text for the button label.
          cancellable: Can it be cancelled?
      """
      title: Text
      body: Text
      button_text: Text
      cancellable: bool


  def create_menu(config: MenuConfig):
      title = config["title"]
      # ...


  create_menu(
      # You need to supply all the parameters
      MenuConfig(
          title="My delicious menu",
          body="A description of the various items on the menu",
          button_text="Order now!",
          cancellable=True
      )
  )
  ```

### Functions should do one thing

- When functions do more than one thing, they are harder to compose, test, and reason about.
- When you can isolate a function to just one action, they can be refactored easily and your code will read much cleaner.

  ```python
  # bad
  from typing import List


  class Client:
      active: bool


  def email(client: Client) -> None:
      pass


  def email_clients(clients: List[Client]) -> None:
      """Filter active clients and send them an email.
      """
      for client in clients:
          if client.active:
              email(client)
  ```

  ```python
  # Good
  from typing import List


  class Client:
      active: bool


  def email(client: Client) -> None:
      pass


  def get_active_clients(clients: List[Client]) -> List[Client]:
      """Filter active clients.
      """
      return [client for client in clients if client.active]


  def email_clients(clients: List[Client]) -> None:
      """Send an email to a given list of clients.
      """
      for client in get_active_clients(clients):
          email(client)
  ```

  ```python
  from typing import Generator, Iterator


  class Client:
      active: bool


  def email(client: Client):
      pass


  def active_clients(clients: Iterator[Client]) -> Generator[Client, None, None]:
      """Only active clients"""
      return (client for client in clients if client.active)


  def email_client(clients: Iterator[Client]) -> None:
      """Send an email to a given list of clients.
      """
      for client in active_clients(clients):
          email(client)
  ```

### Function names should say what they do

```python
# Bad
class Email:
    def handle(self) -> None:
        pass

message = Email()
# What is this supposed to do again?
message.handle()
```

```python
class Email:
    def send(self) -> None:
        """Send this message"""

message = Email()
message.send()
```

### Functions should only be one level of abstraction

```python
# Bad

def parse_better_js_alternative(code: str) -> None:
    regexes = [
        # ...
    ]

    statements = code.split('\n')
    tokens = []
    for regex in regexes:
        for statement in statements:
            pass

    ast = []
    for token in tokens:
        pass

    for node in ast:
        pass
```

```python
from typing import Tuple, List, Text, Dict


REGEXES: Tuple = (
   # ...
)


def parse_better_js_alternative(code: Text) -> None:
    tokens: List = tokenize(code)
    syntax_tree: List = parse(tokens)

    for node in syntax_tree:
        pass


def tokenize(code: Text) -> List:
    statements = code.split()
    tokens: List[Dict] = []
    for regex in REGEXES:
        for statement in statements:
            pass

    return tokens


def parse(tokens: List) -> List:
    syntax_tree: List[Dict] = []
    for token in tokens:
        pass

    return syntax_tree
```

### Don't use flags as function parameters

- Don't use boolean flag as a parameter if you will check it inside our function

  ```python
  # Bad
  from typing import Text
  from tempfile import gettempdir
  from pathlib import Path


  def create_file(name: Text, temp: bool) -> None:
      if temp:
          (Path(gettempdir()) / name).touch()
      else:
          Path(name).touch()
  ```

  ```python
  from typing import Text
  from tempfile import gettempdir
  from pathlib import Path


  def create_file(name: Text) -> None:
      Path(name).touch()


  def create_temp_file(name: Text) -> None:
      (Path(gettempdir()) / name).touch()
  ```

### Avoid side effects

- A function produces a side effect if it does anything other than take a value in and return another value or values.
- A side effect could be writing to a file, modifying some global variable, or accidentally wiring all your money to a stranger.
- Don't have several functions and classes that write to a particular file - rather, have one (and only one) service that does it.
- The main point is to avoid common pitfalls like sharing state between objects without any structure, using mutable data types that can be written to by anything, or using an instance of a class, and not centralizing where your side effects occur.
- Bad <br />

  ```python
  # type: ignore

  # This is a module-level name.
  # It's good practice to define these as immutable values, such as a string.
  # However...
  fullname = "Ryan McDermott"

  def split_into_first_and_last_name() -> None:
      # The use of the global keyword here is changing the meaning of the
      # the following line. This function is now mutating the module-level
      # state and introducing a side-effect!
      global fullname
      fullname = fullname.split()

  split_into_first_and_last_name()

  # MyPy will spot the problem, complaining about 'Incompatible types in
  # assignment: (expression has type "List[str]", variable has type "str")'
  print(fullname)  # ["Ryan", "McDermott"]

  # OK. It worked the first time, but what will happen if we call the
  # function again?
  ```

- Good <br />

  ```python
  from typing import List, AnyStr


  def split_into_first_and_last_name(name: AnyStr) -> List[AnyStr]:
      return name.split()

  fullname = "Ryan McDermott"
  name, surname = split_into_first_and_last_name(fullname)

  print(name, surname)  # => Ryan McDermott
  ```

- Also good

  ```python
  from typing import Text
  from dataclasses import dataclass


  @dataclass
  class Person:
      name: Text

      @property
      def name_as_first_and_last(self) -> list:
          return self.name.split()


  # The reason why we create instances of classes is to manage state!
  person = Person("Ryan McDermott")
  print(person.name)  # => "Ryan McDermott"
  print(person.name_as_first_and_last)  # => ["Ryan", "McDermott"]
  ```

### Don't repeat yourself (DRY)

- Avoid duplicate code
- Getting the abstraction right is critical. Bad abstractions can be worse than duplicate code
- Bad <br />

  ```python
  from typing import List, Text, Dict
  from dataclasses import dataclass

  @dataclass
  class Developer:
      def __init__(self, experience: float, github_link: Text) -> None:
          self._experience = experience
          self._github_link = github_link

      @property
      def experience(self) -> float:
          return self._experience

      @property
      def github_link(self) -> Text:
          return self._github_link

  @dataclass
  class Manager:
      def __init__(self, experience: float, github_link: Text) -> None:
          self._experience = experience
          self._github_link = github_link

      @property
      def experience(self) -> float:
          return self._experience

      @property
      def github_link(self) -> Text:
          return self._github_link


  def get_developer_list(developers: List[Developer]) -> List[Dict]:
      developers_list = []
      for developer in developers:
          developers_list.append({
          'experience' : developer.experience,
          'github_link' : developer.github_link
              })
      return developers_list

  def get_manager_list(managers: List[Manager]) -> List[Dict]:
      managers_list = []
      for manager in managers:
          managers_list.append({
          'experience' : manager.experience,
          'github_link' : manager.github_link
              })
      return managers_list

  ## create list objects of developers
  company_developers = [
      Developer(experience=2.5, github_link='https://github.com/1'),
      Developer(experience=1.5, github_link='https://github.com/2')
  ]
  company_developers_list = get_developer_list(developers=company_developers)

  ## create list objects of managers
  company_managers = [
      Manager(experience=4.5, github_link='https://github.com/3'),
      Manager(experience=5.7, github_link='https://github.com/4')
  ]
  company_managers_list = get_manager_list(managers=company_managers)
  ```

- Good <br />

  ```python
  from typing import List, Text, Dict
  from dataclasses import dataclass

  @dataclass
  class Employee:
      def __init__(self, experience: float, github_link: Text) -> None:
          self._experience = experience
          self._github_link = github_link

      @property
      def experience(self) -> float:
          return self._experience

      @property
      def github_link(self) -> Text:
          return self._github_link



  def get_employee_list(employees: List[Employee]) -> List[Dict]:
      employees_list = []
      for employee in employees:
          employees_list.append({
          'experience' : employee.experience,
          'github_link' : employee.github_link
              })
      return employees_list

  ## create list objects of developers
  company_developers = [
      Employee(experience=2.5, github_link='https://github.com/1'),
      Employee(experience=1.5, github_link='https://github.com/2')
  ]
  company_developers_list = get_employee_list(employees=company_developers)

  ## create list objects of managers
  company_managers = [
      Employee(experience=4.5, github_link='https://github.com/3'),
      Employee(experience=5.7, github_link='https://github.com/4')
  ]
  company_managers_list = get_employee_list(employees=company_managers)
  ```

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Python beyond beginner stage](https://towardsdatascience.com/python-beyond-beginner-stage-good-practices-and-tools-75ddd55b445d) <span id="content-4"></span>

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
- The key is Path object instantiated by passing a string like ./ which is an object representing the path. The object has methods and properties like is_file() , exists() , name , glob('\*.jpeg')
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

<br />

---

## [Advanced Python: Consider These 10 Elements When You Define Python Functions](https://betterprogramming.pub/advanced-python-consider-these-10-elements-when-you-define-python-functions-61c0be8a10ed) <span id="content-5"></span>

### Introduction

- Functions are essential parts of any code project because they’re responsible for preparing and processing data and configuring user interface elements.
- Writing good functions is critical to building a resilient code base.
- With the growth of the project scope, the functions can get far more complicated and the need for more functions grows exponentially.
- Applying best practices to function declarations becomes more important as the scope of your project grows.

### 1. General Guidelines

#### Explicit and meaningful names

- As you know, functions are also objects in Python, so when we define a function, we basically create a variable of the function type. So, the variable name (i.e. the name of the function) has to reflect the operation it performs.
- If you have to write extensive comments to explain your functions, it’s very likely that your functions don’t have good names.
- Example:

  ```python
  # Too generic, wanting others to guess what it does??
  def foo(): pass

  # Lack of details, requiring contexts to understand
  def do_step1(): pass

  # Not following naming conventions, which should be snake style and all lowercase
  def GETData(): pass

  # A few explicit and meaningful names
  def get_account_info(): pass

  def generate_sales_report(): pass
  ```

- Something else to note is that if your functions are intended to be used within your class or module, you may want to prefix the name with an underscore (e.g., def \_internal_fun():) to indicate that these functions are for private usages and they’re not public APIs.

#### Small and Single Purpose

- Your functions should be kept small, so they’re easier to manage.
- If the functions are all enormous in size, your construction won’t progress as smoothly as it could.
- When they’re small, they’re easier to fit into various places and moved around if the need arises.
- It’s also key for your functions to serve single purposes, which can help you keep your functions small.
- Another benefit of single-purpose functions is that you’ll find it much easier to name such functions.
- You can simply name your function based on its intended single purpose.
- Example:

  ```python
  # Embed all operations with one single function
  def process_data():
      # a bunch of code to read data
      # a bunch of code to clean the data
      # a bunch of code to generate the report
      pass

  # Refactor by create additional smaller functions
  def read_data_from_path(filepath):
      return data

  def clean_data(data):
      return cleaned_data

  def generate_report(cleaned_data):
      return report

  def process_data():
      data = read_data_from_path(filepath="path_to_file.csv")
      cleaned_data = clean_data(data)
      report = generate_report(cleaned_data)
      return report
  ```

#### Don’t reinvent the wheel

- It’s essential to be familiar with common functions in standard libraries.
- Before you define your own functions, think about whether the particular business need is common.
- For another instance, if you want to count elements in a list, you should consider the Counter class in the collections module, which is designed specifically for these operations.

### 2. Default Arguments

#### Relevant scenarios

- We can merge functions with similar features together and pass slightly different arguments.
- You should consider setting a default value to the less varied argument.

#### Set default arguments

- The benefit of setting default arguments is straightforward — you don’t need to deal with setting unnecessary arguments in most cases.
- We can look for the real example on `sorted` function. We can use `sorted` in the most simple way, but we can also change the default setting by specifying `reverse` and `key` arguments.
- In terms of what value we should set, the rule of thumb is you should choose the default value that is to be used for most function calls.
- Example:

  ```python
  # Set the price to the sale price or clearance sale with has addition discount
  def set_regular_sale_price(price, discount):
      price *= discount
      return price


  def set_clearance_sale_price(price, discount, additional_discount):
      sale_price = set_sale_price(price, discount)
      return sale_price * additional_discount


  # A refactored combined function
  def set_sale_price(price, discount, additional_discount=1):
      sale_price = price * discount
      return sale_price * additional_discount
  ```

#### Avoid the pitfalls of mutable default arguments

- If your argument is a mutable object, it’s important that you don’t set it using the default constructor — because functions are objects in Python and they’re created when they’re defined.
- The side effect is that the default argument is evaluated at the time of function declaration, so a default mutable object is created and becomes part of the function.
- Whenever you call the function using the default object, you’re essentially accessing the same mutable object associated with the function.
- Example of how do it the bad way:
  ```python
  >>> def add_item_to_cart(new_item, shopper_name, existing_items=[]):
  ...     existing_items.append(new_item)
  ...     print(f"{shopper_name}'s cart has {existing_items}")
  ...     return existing_items
  ...
  ...
  ... shopping_list_wife = add_item_to_cart("Dress", "Jennifer")
  ... shopping_list_husband = add_item_to_cart("Soccer", "David")
  ...
  Jennifer's cart has ['Dress']
  David's cart has ['Dress', 'Soccer']
  ```
- Example:
  ```python
  def add_item_to_cart(new_item, shopper_name, existing_items=None):
      if existing_items is None:
          existing_items = list()
      existing_items.append(new_item)
      print(f"{shopper_name}'s cart has {existing_items}")
      return existing_items
  ```

### 3. Consider Returning Multiple Values

#### Multiple values in a tuple

- Basically, if we defined a function to return multiple values, we can create a class that somewhat reflects the returned values. But also, we can returned these multiple values as tuple.
- Example:
  ```python
  >>> from statistics import mean, stdev
  ...
  ... def evaluate_test_result(scores):
  ...     scores_mean = mean(scores)
  ...     scores_std = stdev(scores)
  ...     return scores_mean, scores_std
  ...
  ... evaluation_result = evaluate_test_result([1, 1, 1, 2, 2, 2, 6, 6, 6])
  ... print(f"Evaluation Result ({type(evaluation_result)}): {evaluation_result}")
  ...
  Evaluation Result (<class 'tuple'>): (3, 2.29128784747792)
  ```

#### But no more than three

- One value (when a function doesn’t explicitly return anything, it actually returns None implicitly) is best — because everything is straightforward and most users usually expect a function to return only one value.
- In some cases, returning two values is fine, returning three values is probably still OK, but please don’t ever return four values.

### 4. Use Try…Except

- Use try...excecpt block if something can go wrong.
- You embed the code that can possibly go wrong (i.e., raise certain exceptions) in the try clause and the possible exceptions are handled in the except clause.
- It’s typically a good idea to define custom exceptions specific to your tool if you want to give more specific information
- Example:

  ```python
  def get_data_from_file(filepath):
      try:
          with open(filepath) as file:
              computed_value = process_data(file)
      except Exception:
          raise SomeCustomFileException(f"can't open the file at the path: {filepath}")
      return computed_value

  def process_data(file):
      # process the data
      return computed_value
  ```

- In other words, if you expect that users of your functions can set some arguments that result in exceptions in your code, you can define functions that handle these possible exceptions.

### 5. Consider Argument Validation

- The previous function using the try…except statement is sometimes referred to as the EAFP (Easier to Ask Forgiveness than Permission) coding style.
- There is another coding style called LBYL (Look Before You Leap), which stresses the sanity check before running particular code blocks.
- Following the previous example, in terms of applying LBYL to function declaration, the other consideration is to validate your function’s arguments.
- One common use case for argument validation is to check whether the argument is of the right data type.
- Example:
  ```python
  # Check type before running the code
  def add_numbers(a, b):
      if not(isinstance(a, (float, int)) and isinstance(b, (float, int))):
          raise TypeError("Numbers are required.")
      return a + b
  ```

#### Discussion: EAFP vs. LBYL

- Although EAFP is a preferred coding style in the Python world, depending on your use case, you should also consider using LBYL which can provide more user-friendly function-specific error messages than the generic built-in error messages you get with the EAFP style.

### 6. Consider Lambda Functions As Alternatives

#### Functions as parameters of other functions

- Some functions can take another function (or are callable, in general terms) to perform particular operations.
- Example:
  ```python
  >>> # A list of dictionary objects for sorting
  >>> grades = [{'name': 'John', 'score': 97},
  ...           {'name': 'David', 'score': 96},
  ...           {'name': 'Jennifer', 'score': 98},
  ...           {'name': 'Ashley', 'score': 94}]
  >>> def sorting_grade(x):
  ...     return x['score']
  ...
  >>> sorted(grades, key=sorting_grade)
  [{'name': 'Ashley', 'score': 94}, {'name': 'David', 'score': 96}, {'name': 'John', 'score': 97}, {'name': 'Jennifer', 'score': 98}]
  ```

#### Lambda functions as alternatives

- A lambda function is an anonymous function declared using the lambda keyword. It takes zero to more arguments and has one expression for applicable operations with the form: lambda arguments: expression.
- Example:
  ```python
  >>> sorted(grades, key=lambda x: x['score'])
  [{'name': 'Ashley', 'score': 94}, {'name': 'David', 'score': 96}, {'name': 'John', 'score': 97}, {'name': 'Jennifer', 'score': 98}]
  ```

### 7. Consider Decorators

#### Decorators

- Decorators are functions that modify the behavior of other functions without affecting their core functionalities.
- In other words, they provide modifications to the decorated functions at the cosmetic level.
- Example:
  ```python
  >>> # Define a decorator function
  ... def echo_wrapper(func):
  ...     def wrapper(*args, **kwargs):
  ...         func(*args, **kwargs)
  ...         func(*args, **kwargs)
  ...     return wrapper
  ...
  >>> # Define a function that is decorated by echo_wrapper
  ... @echo_wrapper
  ... def say_hello():
  ...     print('Hello!')
  ...
  >>> # Call the decorated function
  ... say_hello()
  Hello!
  Hello!
  ```

#### Use decorators in function declarations

- In essence, the @property decorator converts an instance method to make it behave like a regular attribute, which allows the access of using the dot notation.
- Example:
  ```python
  >>> class Product:
  ...     def __init__(self, item_id, price):
  ...         self.item_id = item_id
  ...         self.price = price
  ...
  ...     @property
  ...     def employee_price(self):
  ...         return self.price * 0.9
  ...
  >>> product = Product(12345, 100)
  >>> product.employee_price
  90.0
  ```
  ```python
  >>> from time import time
  ...
  ... # Create the decorator function
  ... def logging_time(func):
  ...     def logged(*args, **kwargs):
  ...         start_time = time()
  ...         func(*args, **kwargs)
  ...         elapsed_time = time() - start_time
  ...         print(f"{func.__name__} time elapsed: {elapsed_time:.5f}")
  ...
  ...     return logged
  ...
  ... @logging_time
  ... def calculate_integer_sum(n):
  ...     return sum(range(n))
  ...
  ... @logging_time
  ... def calculate_integer_square_sum(n):
  ...     return sum(x*x for x in range(n))
  ...
  >>> calculate_integer_sum(10000)
  calculate_integer_sum time elapsed: 0.00027
  >>> calculate_integer_square_sum(10000)
  calculate_integer_square_sum time elapsed: 0.00110
  ```

### 8. Use \*args and \*\*kwargs — But Parsimoniously

- In essence, we use \*args to capture all (or an undetermined number of, to be more general) position arguments while \*\*kwargs to capture all (or an undetermined number of, to be more general) keyword arguments.
- Specifically, position arguments are based on the positions of the arguments that are passed in the function call, while keyword arguments are based on setting parameters to specifically named function arguments.
- If you’re unfamiliar with these terminologies, here’s a quick peek to the signature of the built-in sorted() function: `sorted(iterable, *, key=None, reverse=False)`. The iterable argument is a position argument, while the `key` and `reverse` arguments are keyword arguments.
- Example:
  ```python
  >>> # Define a function that accepts undetermined position arguments
  >>> def stringify(*args):
  ...     return [str(x) for x in args]
  ...
  >>> stringify(2, False, None)
  ['2', 'False', 'None']
  ```
- However, in most cases, you don’t need to use \*args or \*\*kwargs. Although it can make your declaration a bit cleaner, it hides the function’s signature.
- In other words, the users of your functions have to figure out exactly what parameters your functions take. So my advice is to avoid using them if you don’t have to.

### 9. Type Annotation for Arguments

- Python is a dynamically-typed programming language as well as an interpreted language, the implication of which is that Python doesn’t check code validity, including type compatibility, during coding time.
- It's better for us to use type annotation.
- Luckily, IDE can help us detect wrong type.

### 10. Responsible Documentation

- If your functions are for private uses, you don’t have to write very thorough documentation — you can make the assumption that your code tells the story clearly.
- Here, the discussion of responsible documentation is more concerned with the docstrings of your function as public APIs. The following aspects should be included:
  - A brief summary of the intended operation of your function. This should be very concise. In most cases, the summary shouldn’t be more than one sentence.
  - Input arguments: Type and explanation. You need to specify what type of your input arguments should be and what they can do by setting particular options.
  - Return Value: Type and explanation. Just as with input arguments, you need to specify the output of your function. If it doesn’t return anything, you can optionally specify None as the return value.

**[⬆ back to top](#list-of-contents)**

<br />

---

## [How To Write Clean Code in Python](https://betterprogramming.pub/how-to-write-clean-code-in-python-5d67746133f2) <span id="content-6"></span>

### Introduction

- Clean code is code that is easy to understand and easy to change or maintain
- As code is more often read than written, constantly reminding ourselves to practice writing clean code is crucial in our career.

### TL;DR

- Be consistent when naming things
- Eliminate room for confusion when naming things
- Avoid double negatives
- Write self-explanatory code
- Do not abuse comments

### 1. Name Things Properly

- If I name it like this, could it possibly mean something else or confuse other people?
- The general idea here is to always eliminate any room for confusion while naming anything.
- Example:

  ```python
  # For example, you're naming a variable that represents the user’s membership expiration:

  # Example 1
  # ^^^^^^^^^
  # Don't
  expired = True

  # Do
  is_expired = True

  # Example 2
  # ^^^^^^^^^
  # Don't
  expire = '2021-04-17 03:25:37.403283'

  # Do
  expiration_date = '2021-04-17 03:25:37.403283' # OR
  expiration_date_string = '2021-04-17 03:25:37.403283'
  ```

- Nothing should be named solely based on your individual preferences.
- Example:

  ```python
  # For example if the existing project names a Response object as "res" already:

  # Existing functions
  # ^^^^^^^^^^^^^^^^^^
  def existing_function(res, var):
    # Do something...
    pass

  def another_existing_function(res, var):
    # Do something...
    pass

  # Example 1
  # ^^^^^^^^^
  # Don't
  def your_new_function(response, var):
    # Do something...
    pass

  # Do
  def your_new_function(res, var):
    # Do something...
    pass
  ```

- Extra tips when choosing names:
  - Variables are nouns
  - Functions that do something are verbs (i.e. def compute_user_score()).
  - Boolean variables or functions returning boolean are questions (i.e. def is_valid()).
  - Names should be descriptive but not overly verbose (i.e. def compute_fibonacci() rather than def compute_fibonacci_with_dynamic_programming()).

### 2. Avoid Double Negatives

- Example:

  ```python
  # Example to check if a user's membership is valid or not:

  # Don't
  is_invalid = False
  if not is_invalid:
      print("User's membership is valid!")

  # Do
  is_valid = True
  if not is_valid:
      print("User's membership is invalid!")
  ```

- If you have to read it more than once to be sure, it smells.

### Write Self-Explanatory Code

- Engineers need to write self-explanatory code that makes sense to people.
- We should try to capture a complicated piece of logic in a descriptive and self-reading variable.
- Example:

  ```python
  # Don't write long conditionals
  if meeting and (current_time > meeting.start_time) and (user.permission == 'admin' or user.permission == 'moderator') and (not meeting.is_cancelled):
       print('# Do something...')

  # Do capture them in multiple variables that reads like English
  is_meeting_scheduled = meeting and not meeting.is_cancelled
  has_meeting_started = current_time > meeting.start_time
  has_user_permission = user.permission == 'admin' or user.permission == 'moderator'
  if is_meeting_scheduled and has_meeting_started and has_user_permission:
      print('# Do something...')
  ```

- Whenever you feel the need to write a comment, you should always re-evaluate the code you have just written to see how it could be made clearer.
- Example of when to write comments:

  ```python
  # Example of getting an email returned from a 3rd party API:

  # Example 1
  # ^^^^^^^^^
  # Do
  raw_string = get_user_info()
  email = raw_string.split('|', maxsplit=2)[-1]  # NOTE: raw_string e.g. "Magic Rock|jerry@example.com"
  ```

  ```python
  # Example of a function calling a random time.sleep():

  # Example 2
  # ^^^^^^^^^
  # Don't
  def create_user(user_ids):
      for id in user_ids:
          make_xyz_api_request(id)
          time.sleep(2)

  # Do
  def create_user(user_ids):
      for id in user_ids:
          make_xyz_api_request(id)
          time.sleep(2) # NOTE: service 'xyz' has a rate limit of 100 requests/min, so we should slow our requests down
  ```

- Always put yourself in others’ shoes (i.e. “How would the others interpret my code?”).

### How Do I Apply This Knowledge?

- No one is capable of writing clean code from day one. As a matter of fact, everyone starts by writing “bad” or “ugly” code.
- Besides practicing, here are the things that work for me:
  - Keep asking yourself questions like “Is there a better way of writing it? Is this confusing for others to read?”
  - Take part in code reviews.
  - Explore other well-written code bases. If you want some examples of well-written, clean, and Pythonic code, check out the Python requests library.
  - Talk to people, discuss or exchange opinions, and you will learn a lot more quickly.

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Best Practices To Follow While Creating Classes In Python](https://medium.com/pythoneers/best-practices-to-follow-while-creating-classes-in-python-4497bc8535dc) <span id="content-7"></span>

### Introduction

- A Class in oop Works as a blueprint for the object. if we define a car as a class then different brands or types of cars will be objects.

### 1. Use Inheritance Instead of redefining variables

- Inheritance is one of the four pillars of OOP. It is the process by which one class inherits the properties of another class. The Class that inherits properties from another class is called child and the other one is called the Parent class.
- Inheritance can help us to reduce the code and make it look more readable and professional.
- Example:

  ```python
  class Employee:
    def __init__(self,name,age,exp,salary):
      self.name = name
      self.age = age
      self.exp = exp
      self.salary = salary

  class Developers(Employee):
    def __init__(self,name,age,exp,salary,level):
        super().__init__(name,age,exp,salary)
        self.level = level

  class Deginers(Employee):
    def __init__(self,name,age,exp,salary,level):
      super().__init__(name,age,exp,salary)
      self.level = level
  ```

### 2. Class vs Static vs Instance Method (Use Wisely)

- In python, you can define three kinds of methods. Static, Class, and Instance.
- Instance Methods are simple methods that you create while creating classes. These methods are concerned with individual instance objects. These methods are defined Like this: def do_something(self): , here self refers to the instance object that calls the method.
- Class Methods are different kinds of methods. They are bound to the class, not with the object of the class. These methods can access and modify the state of the class. It requires the class as a parameter to the method. To create a class method we use @classmethoddecorator. It can be used to do factory tasks.
- Static Methods are concerned with a particular state of the class. They can not access or modify the state of the class. Static methods do not take any specific parameter as input. To create a static method we use @staticmethod , It can be used to do utility tasks.
- The difference between both is that class methods allow you to access or update attributes related to the class, while static methods are only concerned with an instance or the class itself.
- Example:

  ```python
  class A(object):
      def foo(self, x):
          print(f"executing foo({self}, {x})")

      @classmethod
      def class_foo(cls, x):
          print(f"executing class_foo({cls}, {x})")

      @staticmethod
      def static_foo(x):
          print(f"executing static_foo({x})")
  a = A()
  ```

### 3. use @property

- The Property decorator is a built-in decorator in python that helps to define properties without explicitly calling the property() function. It can also offer the functionality to define getters and setters.
- Example:

  ```python
  class Data:
      def __init__(self, fname, lname):
          self.fname = fname
          self.lname = lname

      @property
      def name(self):
          print("Getter")
          return f"{self.fname} {self.lname}"

      @name.setter
      def name(self, name):
          print("Setter")
          self.fname, self.lname = name.split()

  obj = Data("Jack", "Davidson")
  print("Student Name:", obj.name)
  obj.name = "Jake Davidson"
  print("After setting:", obj.name)

  '''output
  Getter
  Student Name: Jack Davidson
  Setter
  Getter
  After setting: Jake Davidson
  '''
  ```

### 4. Consider Using **slots** For Optimization

- If Most of the time your class is used as a data container for storing data only, then you can use **slots** it to optimize the performance of the class.
- In general, When we create a class it is automatically backed by a dictionary **dict** that is used to store all the information about instance variables inside the class.
- Example of properties as dictionary:
  ```python
  class A:
     pass
  a = A()
  print(a.__dict__)
  > {}  ##Empty Dictionary will be used to store Values of instances
  ## Let's assign a value to the instance
  a.x = 5
  print(a.__dict__)
  >{'x': 5}  ## The Instance value gets stored in the dictionary
  ## Let's Create one more instance
  b.x = 5
  print(b.__dict__)
  print(a.__dict__)
  >{'x':5}
  {'y':6}
  ```
- As shown in the above example, every time we create a new instance a new dictionary gets created for that instance. suppose if you have to create a thousand instances then thousand dictionaries also get created. It will automatically increase the size of memory.
- Example of using `__slots__` to specify class' properties
  ```python
  class B:
     __slots__ = ('x','y')
     pass
  obj = B()
  obj.x = 10
  print(obj.__dict__)
  ---------OUTPUT------
  Traceback (most recent call last):
    File "main.py", line 6, in <module>
      print(obj.__dict__)
  AttributeError: 'B' object has no attribute '__dict__'
  ```
- If you try to inherit from a class that contains slots then the child class will reset the slots and you will again see dict for storing values of the instance. It is because slots work at each level of class inheritance and if you inherit one class from another then it gets reset after the parent level.

### 5. Magic Methods

- 1. `__init__`: for class creation
- 2. `__str__`: It is an object representation method. It returns a printable string representation of any user-defined class.
- 3. `__add__`: For addition, based on the defined class

**[⬆ back to top](#list-of-contents)**

<br />

---

## [11 Refactoring Patterns To Elevate Your Python Code](https://betterprogramming.pub/11-refactoring-patterns-to-elevate-your-python-code-a47dbe5826d) <span id="content-8"></span>

### Introduction

- Refactoring is a disciplined technique for restructuring an existing body of code, altering its internal structure without changing its external behavior.
- Refactoring is a disciplined technique for restructuring an existing body of code, altering its internal structure, that may also cause its external behavior to change.
- If you can add a small or large amount of functionality to an application, framework, package, or code set, you are refactoring that code set.

### 1. Remove Unneeded Comments

### 2. Assign Constants to Variables

- Putting constants into variables enables them to be located in one place. If they are located in one place, it is of much lower cost to change them and lower cost to maintain the code set.
- Example:
  ```python
  ELEMENT_TYPES = ['Classification','Regression', 'Clustering']
  CLSFID = 0
  REGRID = 1
  CLSTID = 3
  SCORE_TYPES = ['score','error', 'un-supervised']
  SCOREID = 0
  ERRORID = 1
  UNSUPID = 2
  ```

### 3. Bug Fixing or Adding New Code

- Adding clustering and all associated code adds and changes results in substantial architecture refactoring.

### 4. Modifying Keys in a Dictionary

- Example (before):
  ```python
  ELEMENT_DICTIONARY = {
      # Classification
      'accuracy': ('sklearn.metrics', 'accuracy_score', 'score'),
      'f1_score': ('sklearn.metrics', 'f1_score', 'score'),
      'hamming_loss': ('sklearn.metrics', 'hamming_loss', 'error'),
      'log_loss': ('sklearn.metrics', 'log_loss', 'error'),
      'precision': ('sklearn.metrics', 'precision_score', 'score'),
      'recall': ('sklearn.metrics', 'recall_score', 'score'),
      'auc': ('sklearn.metrics', 'roc_auc_score', 'score'),
  .
  .
  .
  ```
- Example (after):
  ```python
  ELEMENT_SCORES = {
      ELEMENT_TYPES[CLSFID] : {     # Classification
          'accuracy': ('sklearn.metrics', 'accuracy_score', SCORE_TYPES[SCOREID]),
          'f1_score': ('sklearn.metrics', 'f1_score', SCORE_TYPES[SCOREID]),
          'hamming_loss': ('sklearn.metrics', 'hamming_loss', SCORE_TYPES[ERRORID]),
          'log_loss': ('sklearn.metrics', 'log_loss', SCORE_TYPES[ERRORID]),
          'precision': ('sklearn.metrics', 'precision_score', SCORE_TYPES[SCOREID]),
          'recall': ('sklearn.metrics', 'recall_score', SCORE_TYPES[SCOREID]),
          'auc': ('sklearn.metrics', 'roc_auc_score', SCORE_TYPES[SCOREID]),
  .
  .
  .
  ```

### 5. Transforming Duplicate Code Into Decorators

- Python has an excellent solution for code that has a repetitive pattern at the top or bottom or both. The solution is a wrapper that can go around the differencing middle code, called a decorator in Python.
- Example:
  ```python
  # adapted from pandas-flavor
  from pandas.api.extensions import register_dataframe_accessor
  def register_DataFrame_method(method):
      """Register a function as a method attached to the
      Pandas  DataFrame.
      Example
      -------
      for a function
          @pf.register_dataframe_method
          def row_by_value(df, col, value):
          return df[df[col] == value].squeeze()
      for a class method
          @pf.register_dataframe_accessor('Aclass')
          class Aclass(object):
          def __init__(self, data):
          self._data
          def row_by_value(self, col, value):
              return self._data[self._data[col] == value].squeeze()
      """
  from typing import Callable
  def inner(*args, **kwargs):
          class AccessorMethod(object):
              def __init__(self, pandas_obj):
                  self._obj = pandas_obj
              @wraps(method: Callable)
              def __call__(self, *args, **kwargs):
                  return method(self._obj, *args, **kwargs)
          register_dataframe_accessor(method.__name__)(AccessorMethod)
          return method
      return inner()
  ```

### 6. Transforming Python>3.7 Classes Into Python≤3.7 @dataclass

-` @dataclass` implements a `__init__()` method for argument initialization, a `__repr__()` method for string representation, and the` __eq__()` method for object comparisons.

- Example:
  ```python
  ##########   BEFORE
  class CrossValidation:
      def __init__(self, inner_cv, outer_cv,
                   eval_final_performance, test_size,
                   calculate_metrics_per_fold,
                   calculate_metrics_across_folds):
          self.inner_cv = inner_cv
          self.outer_cv = outer_cv
          self.eval_final_performance = eval_final_performance
          self.test_size = test_size
          self.calculate_metrics_per_fold = calculate_metrics_per_fold
          # Todo: if self.outer_cv is LeaveOneOut: Set calculate metrics across folds to True -> Print
          self.calculate_metrics_across_folds = calculate_metrics_across_folds
          self.outer_folds = None
          self.inner_folds = dict()
  from dataclasses import dataclass
  ##########   AFTER
  from dataclasses import dataclass, field
  from typing import Any, Dict
  @dataclass
  class CrossValidation:
      inner_cv: int
      outer_cv: int
      eval_final_performance: float
      test_size: int
      calculate_metrics_per_fold: bool
      # Todo: if outer_cv is LeaveOneOut: Set calculate metrics across folds to True -> Print
      calculate_metrics_across_folds: bool
      inner_folds: Dict = field(default_factory=dict)
      outer_folds: Any = None
  ```

### 7. Eliminate Unnecessary Code Statements

- If you want to produce clean, readable code, you need to delete unnecessary code and comments.

### 8. Code Hoisting

- Code hoisting is the child pattern of the eliminate-unnecessary-code-statements pattern.
- Code hoisting occurs when a statement or statements appear on two or more conditional branches. Those redundant statements are “hoisted” out of the conditional.
- Example:
  ```python
  ##########   BEFORE
  if self.maximize_metric:
      # max metric
      best_config_metric_nr = np.argmax(list_of_scores)
  else:
      # min metric
      best_config_metric_nr = np.argmin(list_of_scores)
  ##########   AFTER
  best_config_metric_nr = np.argmin(list_of_scores)
  if self.maximize_metric:
      best_config_metric_nr = np.argmax(list_of_scores)
  ```

### 9. Document the Code

### 10. Put In Type Hints

- Example:

  ```python

  def toContinuousCategory(
      oX: pd.DataFrame,
      features: list = [],
      drop: bool = True,
      int_: bool = True,
      float_: bool = True,
      quantile: bool = True,
      nbin: int = 10,
      inplace: bool = True,
      verbose: bool = True,
  ) -> pd.DataFrame:
  ```

### 11. Update the Test Suite

- Guidelines:
  - The code must follow PEP-8 format style guidelines.
  - The test suite must be of 85+% coverage of the code set.
  - There must be one or more tests for any changed function or method.
  - There must be one or more tests for any new function, method class, and data class.
  - The test suite must be automate-able.

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Python Refactoring Tips to Write Code in Pythonic Way](https://levelup.gitconnected.com/python-refactoring-tips-to-write-code-in-pythonic-way-6b8ff4375b3a) <span id="content-9"></span>

### Introduction

- Refactoring your code not only makes your code more readable but also reduces the number of unnecessary lines.
- It’s your responsibility to make your code more readable so that others can read it easily and understand what logic you have implemented to solve any particular problem.

### 1. Pull Statements out of the Loop

- Example:
  ```python
  for address in addresses:
      city = "New York"
      location.append(address.street_address, city)
  ```
- In the above example, declaring the variable in the loop is unnecessary as the variable’s value is never changed.
- Since the variable is never changing within the for loop. It's better to write the code like this:
  ```python
  city = "New York"
  for address in addresses:
      location.append(address.street_address, city)
  ```

### 2. Merged nested If statements

- Example:
  ```python
  if a > 5:
      if b < 10:
          print("Checking conditions")
  ```
- Make the nested if into a single statement:
  ```python
  if a > 5 and b < 10:
       print("Checking conditions")
  ```

### 3. Simplify sequence check

- Example:
  ```python
  if len(list_of_fruits) > 0:
     fruit_to_eat = choose_fruit(list_of_fruits)
  ```
- Improved:
  ```python
  if list_of_fruits:
      fruit_to_eat = choose_fruit(list_of_fruits)
  ```
- My personal opinion would be the first example is better because of the explicitness. The second example is a bit implicit about the purpose of the if statement,

### 4. Use Any instead of Loop

- Here’s the code to check negative numbers:
  ```python
  nums = [1,5,7,9,-3, 15]
  flag = False
  for num in nums:
      if num < 0:
          flag = True
          break
  ```
- Using any to achieve the same result as the above code:
  ```python
  nums = [1,5,7,9,-3,15]
  flag = any(num<0 for num in nums)
  ```

### 5. Remove inline variables that are used once only

- Example:
  ```python
  def sum(a, b):
      total = a + b
      return total
  ```
- To remove the redundant variable declaration from the above example. It's better to write the code like this:
  ```python
  def sum(a, b):
      return a+b
  ```

### 6. Replace If statement with If expression

- Example:
  ```python
  if condition:
      flag = True
  else:
      flag = False
  ```
- The refactored code. Using inline if expression:
  ```python
  flag = True if condition else False
  ```

### 7. Adding a Guard Clause

- Example:
  ```python
  def do_i_need_hat(self, hat):
      if isInstance(hat, Hat):
          weather_outside = getWeatherReport()
          if weather_outside.is_raining:
              print("Yes")
              return True
          else:
              return False
      else:
          return False
  ```
- Refactored by inverting the flow. Bad case or special case needs to be handled first.
  ```python
  def do_i_need_hat(self, hat):
      if not isInstance(hat, Hat):
          return False
  if isInstance(hat, Hat):
          weather_outside = getWeatherReport()
          if weather_outside.is_raining:
              print("Yes")
              return True
          else:
              return False
  ```

**[⬆ back to top](#list-of-contents)**

<br />

---

## [12 Of My Favorite Python Practices For Better Functions](https://towardsdatascience.com/12-of-my-favorite-python-practices-for-better-functions-7a21d18cfb38) <span id="content-10"></span>

### Input / Output

- Ultimately, the destiny of a function is a return, or to alter something.
- First ask what do we need to get out of the function? This is our output.
- Example:
  ```python
  def mean(x : list):
      return(mu)
  ```
  ```python
  def mean(x : list):
      mu = sum(x) / len(x)
      return(mu)
  ```

### Extraction

- xtraction is simply creating more methods in order to handle multiple things inside of one function without said function being a scavenger hunt for different values that we need.
- Functions should be simple and have short directives.
- It is going to be much more difficult to stack-trace a bug if that bug is contained within a function that is a mile long.
- Example:
  ```python
  from numpy import sqrt
  def norm(x : list):
      mu = sum(x) / len(x)
       x2 = [(i-mu) ** 2 for i in x]
       m = sum(x2) / len(x2)
       std = sqrt(m)
        return([(i - mu) / std for i in x])
  ```
- Example:
  ```python
  def mean(x : list):
      return(sum(x) / len(x))
  def std(x : list):
      mu = sum(x) / len(x)
      x2 = [(i-mu) ** 2 for i in x]
      m = sum(x2) / len(x2)
      return(sqrt(m))
  def betternorm(x : list):
      mu = mean(x)
      st = std(x)
      return([(i - mu) / st for i in x])
  ```

### NAMING

- Names are important, because in most cases they should tell you the output of the function.
- This function name is not specific.

  ```python
  def pickle(n_pickles : int):
      pass

  def jerry_eat_pickle(n_pickles : int):
    pass
  ```

- Functions need to be named with convenient names.

### No Rewriting

- It is probably a good idea to find some sort of way to not repeat the code that you write over and over again.

### Less Is Superior

- Less code is always superior to more code.
- Usually, less code will also have a significant benefit to performance costs. That being said, having less code will also always be easier to read, which is actually more important than performance in many situations.

### RESTRICT TYPES

- A huge mistake that many beginners make when they start to develop their first Python modules and functions is not restricting the types of their arguments.
- Another reason you might want to set your arguments’ types is so that the interpreter is aware of the type that you might be working with in the function prior to the type ever being passed.

### DOC STRINGS!

- oc strings are absolutely vital — you simply cannot operate effectively without them. As a human, you are bound to forget things. There is no way you could remember what a module of 10,000 lines of code spread across 10 files does in every individual capacity.

### Minimal Nesting

- Another common rookie mistake in the programming world is too much nesting.
- Nesting is a term that is used anytime there is a new level of scope declared inside of a given piece of software.

### (Python) Decorators

### Code Your Comments

- If you have a code file that is 500 lines of code and 500 lines of comments, you are probably using comments wrong.
- Avoid making obvious remarks, such as:
  ```python
  # get parameters
  parameters = get_params(data)
  ```

### Use lambda!

- Another great tip for writing functions is not to write a function at all. Instead, you can write an expression using the lambda key-word.
- This will effectively turn your Python function into a 1-line statement that can be mapped to arrays.

### Avoid KWARGS (as possible)

- They are incredibly useful, especially for things like parameters we use for plotting or machine-learning software.

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Write Clean Python Code Using Pipes](https://towardsdatascience.com/write-clean-python-code-using-pipes-1239a0f3abf5) <span id="content-11"></span>

### Motivation

- Example:
  ![](https://miro.medium.com/max/2000/1*8D5THbKGu368fgqNXvUAqQ.png)
- Harder to read with nested lambda functions
- Solution using Pipe:
  ![](https://miro.medium.com/max/1400/1*tUI5sEgmgQ5lhTQOYu9hQg.png)

### What is Pipe?

- Pipe is a Python library that enables you to use pipes in Python. A pipe (|) passes the results of one method to another method.

### Where — Filter Elements in an Iterable

- Similar to SQL, Pipe’s where method can also be used to filter elements in an iterable.
- Example:
  ![](https://miro.medium.com/max/700/1*RKIzK9VpkoVrTgnXBnecWw.png)

### Select — Apply a Function to an Iterable

- The select method is similar to the map method. select applies a method to each element of an iterable.
- In the code below, I use select to multiply each element in the list by 2.
- Example:
  ![](https://miro.medium.com/max/700/1*yxLCiXEKmyspWMMdhQ_bgQ.png)

- Removing nested parantheses while using map and filter:
  ![](https://miro.medium.com/max/700/1*tUI5sEgmgQ5lhTQOYu9hQg.png)

### Unfold Iterables

- chain — Chain a Sequence of Iterables
  ![](https://miro.medium.com/max/700/1*2QjM4mSlQciSPrc9U0D9AQ.png)
- traverse — Recursively Unfold Iterables: The traverse method can be used to recursively unfold iterables. Thus, you can use this method to turn a deeply nested list into a flat list.
  ![](https://miro.medium.com/max/700/1*IgQ736NVc6f_TfRTfF3m_w.png)
- Example:
  ![](https://miro.medium.com/max/700/1*01vApchQJQjewbR3w0-O0w.png)

### Group Elements in a List

- Sometimes, it might be useful to group elements in a list using a certain function. That could be easily done with the groupby method.
- Example:
  ![](https://miro.medium.com/max/2000/1*rh2vSxQZrn7exvB0v4Z59g.png)

### dedup — Deduplicate Values Using a Key

- The dedup method removes duplicates in a list.
- Example:
  ![](https://miro.medium.com/max/700/1*aBYXrm_7w68anKcWEAjm7w.png)
- Get unique elements less than 5:
  ![](https://miro.medium.com/max/700/1*RKnjElOWmA06_ftSmMYmWQ.png)
- Last example:
  ![](https://miro.medium.com/max/700/1*X1eRTaS8h0nv9SeXIKYPPQ.png)

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Python: Production-Level Coding Practices](https://medium.com/red-buffer/python-production-level-coding-practices-4c39246e0233) <span id="content-12"></span>

### Break down the code

- Always limit tasks to their specific functions.
- The software development principle you need to follow is the Separation of Concern
- Both these tasks should be separate functions which are later called to calculate the output.
- Example:
  ```python
  listA = [1, 2, 3, 4, 5]
  listB = [9, 8, 7, 6, 5]
  def find_sum(listA, listB):
    summed_list = np.add(listA, listB)
    return summed_list
  def find_square(my_list):
    squared_list = np.square(my_list)
    return squared_list
  summed_list = find_sum(listA, listB);
  squared_list = find_square(summed_list)
  ```
- This is why the task should be broken down into separate tasks even for smaller steps like element-wise addition or squaring in order to increase reusability and saving time in the long run.

### Start Using a Proper IDE

- Using an IDE (Integrated Development Environment), specifically for your Python codes, is very important and much better than using notebooks.

### Group Files on the Basis of Tasks/Steps

- A very useful way to keep the project code modular is by grouping files in terms of the overall tasks they perform.

### Use config.Py for All Your Directories

- If your work requires you to load a lot of files or go to specific paths, you should mention all such directories or hard-coded values in a configuration file.
- Make sure to have one source of truth.
  ```text
  Config.py >>
  MY_FILE_PATH = "./abc/xyz.csv"
  Task_file >>
  import config
  pandas.read_csv(config.MY_FILE_PATH)
  ```

### Make Config Files for All Environments

- You need to create separate config files for your local, test, and production environments and use a method to programmatically use a particular config file in terms of the environment you are in (like using cross-env in node.js).
- One of the methods you could use in Python for your environments is Argparse. The documentation for Argparse can be found here.

### Use Blueprints for Flask

- Flask Blueprints are a great tool for dealing with application complexity as it increases.

### Try to Optimize Your Code As Much As Possible

- Code Optimization at the production level becomes really important because the user or the client would demand a much-reduced application processing time on simpler non-dev machines.

### Logging Critical Failures and Intermediate Results

- Logging is very important when writing production-level code. You need to track critical failures in your application and find a necessary solution to them.
- I prefer to create a log text file that will show me any error tracebacks or intermediate results. The purpose for getting intermediate results logged is that you can gauge how the app is running and which part has been reached.
  ```python
  # define a path for your log file
  logs_file_path = "./app.log"
  # Create the log file
  sys.stdout = open(logs_file_path, "w", buffering=1, encoding='utf-8')
  ```

### Handle Possible Errors in the Code

- Use Try and Except statements to handle possible errors and log them using traceback.
  ```python
  import traceback
  import sys
  logs_file_path = "./app.log"
  sys.stdout = open(logs_file_path, "w", buffering=1, encoding='utf-8')
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
  try:
    print(thisdict["car"])
  except Exception as i:
    print(traceback.format_exc())
  ```

### Proper Naming to Improve Readability

- The name should at most parts explain itself by its name.

### Create a Proper Project Structure

- Making a great project structure is one of the most important things because that actually aligns your tasks in proper order, and you can make sure that modules are separated from each other properly.

**[⬆ back to top](#list-of-contents)**

<br />

---

## [Python Code Quality: Tools & Best Practices](https://realpython.com/python-code-quality/) <span id="content-13"></span>

### What is Code Quality?

Hopefully, you can agree on the following high-quality code identifiers:

- It does what it is supposed to do.
- It does not contain defects or problems.
- It is easy to read, maintain, and extend.

### Why Does Code Quality Matter?

- It does not do what it is supposed to do <br />
  Meeting requirements is the basis of any product, software or otherwise. We make software to do something. If in the end, it doesn’t do it… well it’s definitely not high quality. If it doesn’t meet basic requirements, it’s hard to even call it low quality.
- It does contain defects and problems <br />
  If things break on edge cases and defects cause unwanted behavior, we don’t have a high-quality product.
- It is difficult to read, maintain, or extend <br />
  If you work with a team of developers, you can start putting into place methods to ensure better overall code quality. Assuming that you have their support, of course. You may have to win some people over (feel free to send them this article 😃).

### Style Guides

- it’s safe to assume that you at least want consistency in code.
- PEP 8 provides coding conventions for Python code. It is fairly common for Python code to follow this style guide. It’s a great place to start since it’s already well-defined.
- A sister Python Enhancement Proposal, PEP 257 describes conventions for Python’s docstrings, which are strings intended to document modules, classes, functions, and methods. As an added bonus, if docstrings are consistent, there are tools capable of generating documentation directly from the code.

### Linters

- First, let’s talk about lint. Those tiny, annoying little defects that somehow get all over your clothes. Clothes look and feel much better without all that lint.
- Linters analyze code to detect various categories of lint. Those categories can be broadly defined as the following:
  - Logical Lint
    - Code errors
    - Code with potentially unintended results
    - Dangerous code patterns
  - Stylistic Lint
    - Code not conforming to defined conventions

### What Are My Linter Options For Python?

- Flake8: Capable of detecting both logical and stylistic lint. It adds the style and complexity checks of pycodestyle to the logical lint detection of PyFlakes. It combines the following linters:
  - PyFlakes
  - pycodestyle (formerly pep8)
  - Mccabe
- Pylama: A code audit tool composed of a large number of linters and other tools for analyzing code. It combines the following:
  - pycodestyle (formerly pep8)
  - pydocstyle (formerly pep257)
  - PyFlakes
  - Mccabe
  - Pylint
  - Radon
  - gjslint
- Pylint
  - The common complaints against Pylint are that it is slow, too verbose by default, and takes a lot of configuration to get it working the way you want.
- PyFlakes
  - Pyflakes “makes a simple promise: it will never complain about style, and it will try very, very hard to never emit false positives”.
  - The downside here is that parsing this output may be a bit more difficult
- pycodestyle (formerly pep8)
  - Used to check some style conventions from PEP8.
- pydocstyle (formerly pep257)
  - Very similar to pycodestyle, except instead of checking against PEP8 code style conventions, it checks docstrings against conventions from PEP257.

### When Can I Check My Code Quality?

- You can check your code’s quality:
  - As you write it
  - When it’s checked in
  - When you’re running your tests
- It’s useful to have linters run against your code frequently. If automation and consistency aren’t there, it’s easy for a large team or project to lose sight of the goal and start creating lower quality code.

**[⬆ back to top](#list-of-contents)**

<br />

---

## References:

- https://towardsdatascience.com/python-clean-code-6-best-practices-to-make-your-python-functions-more-readable-7ea4c6171d60
- https://blog.devgenius.io/clean-code-in-python-8251eea292fa
- https://github.com/zedr/clean-code-python/blob/master/README.md
- https://towardsdatascience.com/python-beyond-beginner-stage-good-practices-and-tools-75ddd55b445d
- https://betterprogramming.pub/advanced-python-consider-these-10-elements-when-you-define-python-functions-61c0be8a10ed
- https://betterprogramming.pub/how-to-write-clean-code-in-python-5d67746133f2
- https://levelup.gitconnected.com/python-refactoring-tips-to-write-code-in-pythonic-way-6b8ff4375b3a
- https://towardsdatascience.com/12-of-my-favorite-python-practices-for-better-functions-7a21d18cfb38
- https://towardsdatascience.com/write-clean-python-code-using-pipes-1239a0f3abf5
- https://realpython.com/python-code-quality/
