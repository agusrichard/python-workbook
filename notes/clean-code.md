# Python Clean Code

</br>

## List of Contents:
### 1. [Python Clean Code: 6 Best Practices to Make Your Python Functions More Readable](#content-1)
### 2. [Clean Code in Python](#content-2)
### 3. [Clean Code Python](#content-3)


</br>

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
- Look at this mouthful code: </br>
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
- Refactored: </br>
  ```python
  import zipfile

  def unzip_data(output: str):
    
      with zipfile.ZipFile(output, 'r') as zip_ref:
          zip_ref.extractall('.')
  ```


### Do One Task
- A function should complete only one task, not multiple tasks.
- Refactored: </br>
  ```python
  download_zip_data_from_google_drive(url, output_path)

  unzip_data(output_path)

  tweet_train, tweet_test = get_train_test_docs(path_train, path_test)
  ```
- Each function should only do one thing


### One Level of Abstraction
- The level of abstraction is the amount of complexity by which a system is viewed or programmed. The higher the level, the less detail. The lower the level, the more detail. — PCMag
- Before: </br>
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
- After being refactored: </br>
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
- This code contains duplication: </br>
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
- Refactored: </br>
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
- If the descriptive name of a function is too long such as download_file_from_ Google_drive_and_extract_text_from_that_file . It is a good sign that your function is doing multiple things and you should split it into smaller functions.
- Variable name has to tell us about what it is and function name has to tell us about what it does


### Have Fewer than 4 Arguments
- A function should not have more than 3 arguments since it is a sign that the function is performing multiple tasks.
- If a function has more than 3 arguments, consider turning it into a class.
- One way to cluster our functions is by using class. This is how it's done: </br>
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


</br>

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
- Now is better than never. Although never is often better than *right* now.
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
- Use decorators: </br>
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
- Context managers: </br>
  ```python
  # Read a File

  file = open("path_file", mode="r")
  print(file.read())
  file.close()

  # Using context managers

  with open("path_file", mode="r") as file:
    print(file.read())
  ```
- Dunder Methods: </br>
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

</br>

---

## [Clean Code Python](https://github.com/zedr/clean-code-python/blob/master/README.md) <span id="content-3"></span>

> Thank you to the author for writing such an awesome summary
### Introduction
- It's a guide to producing readable, reusable, and refactorable software in Python.
- Not every principle herein has to be strictly followed, and even fewer will be universally agreed upon. These are guidelines and nothing more, but they are ones codified over many years of collective experience by the authors of Clean Code.

### Variables
- Use meaningful and pronounceable variable names </br>
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
- Use the same vocabulary for the same type of variable </br>
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
  - Example: </br>
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
- Use explanatory variables </br>
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
  - Don’t force the reader of your code to translate what the variable means. Explicit is better than implicit. </br>
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
  - If your class/object name tells you something, don't repeat that in your variable name. </br>
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
- Use default arguments instead of short circuiting or conditionals </br>
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
- Bad </br>
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
- Good </br>
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
- Bad </br>
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
- Good </br>
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
  


</br>

---
## References:
- https://towardsdatascience.com/python-clean-code-6-best-practices-to-make-your-python-functions-more-readable-7ea4c6171d60
- https://blog.devgenius.io/clean-code-in-python-8251eea292fa
- https://github.com/zedr/clean-code-python/blob/master/README.md