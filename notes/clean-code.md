# Python Clean Code

</br>

## List of Contents:
### 1. [Python Clean Code: 6 Best Practices to Make Your Python Functions More Readable](#content-1)


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


</br>

---


## References:
- https://towardsdatascience.com/python-clean-code-6-best-practices-to-make-your-python-functions-more-readable-7ea4c6171d60