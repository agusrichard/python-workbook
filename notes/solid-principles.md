# Python Clean Code

</br>

## List of Contents:
### 1. [The Single Responsibility Principle in Python](#content-1)


</br>

---

## Contents:

## [The Single Responsibility Principle in Python](https://towardsdatascience.com/the-single-responsibility-principle-in-python-d0ab0a681853) <span id="content-1"></span>

### Introduction
- The Single Responsibility Principle (SRP) states that a function or a class should have one responsibility.
- Examples of Function Responsibilities
  - Getting data from a database is a responsibility.
  - Filtering, sorting, or transforming that data is another responsibility.
  - Storing data is a different responsibility.
  - So is presenting that data to the user.
- Functions that handle more than one responsibility have more than one reason to change.

### Motivating Example: Extracting Data From Archives
- Example:
  ```python
  import os
  import shutil
  import re


  def prepare_files(directory_path):
    
    archive_pattern = re.compile('\.(zip|gz|tar)$')
    
    for filename in os.listdir(directory_path):
      if archive_pattern.search(filename):
        filepath = os.path.join(directory_path, filename)
        shutil.unpack_archive(filepath)
        
  return
  ```
- The above funtion have 3 responsibilities in 5 lines of code:
  - It iterates through the files in the given directory.
  - It determines if the file is an archive.
  - If it identifies the file as an archive, it extracts the files it contains.
- Not every function needs to be continuously split up into smaller sub-functions.


### Refactoring Based on The Single Responsibility Principle
- Refactored:
  ```python
  import os
  import shutil
  import re


  def prepare_files(directory_path):
    
    for archive_path in get_archive_paths(directory_path):
      shutil.unpack_archive(archive_path)
      
    return


  def get_archive_filepaths(directory_path):
    
    archive_paths = []
    for filename in os.listdir(directory_path):
      filepath = os.path.join(directory_path, filename)
      if should_extract(filepath):
        archive_paths.append(filepath)
        
     return archive_paths


  def should_extract(filepath):
    
    archive_pattern = re.compile('\.(zip|gz|tar)$')
    skip_pattern = re.compile('^skip_')
    
    should_extract_bool = False
    if not skip_pattern.search(filepath) and archive_pattern.search(filename):
      should_extract_bool = True
        
    return should_extract_bool
  ```
- Shorter functions are generally better, but not necessarily in this case.
- The 5 lines for building the archive_paths could be made into a one-line list comprehension, but I think the result would be less clear.
- A Rule of Thumb for Using the Single Responsibility Principle
  - Try to describe the purpose of your function fully and succinctly.
  - If you can’t fully describe what your function does in a short sentence without using the word “and,” then your function should probably be split up.
  

### Using the Single Responsibility Principle to Keep Growing Code Organized
- Another example:
  ```python
  import os
  import shutil
  import re


  def prepare_files(directory_path):
    
    for filename in os.listdir(directory_path):
      filepath = os.path.join(directory_path, filename)
      prepare_file(filepath)
      
    return


  def prepare_file(filepath):
    
    archive_pattern = re.compile('\.(zip|gz|tar)$')
    excel_pattern = re.compile('\.(xlsx|xls)$')
    
    if archive_pattern.search(filepath):
      shutil.unpack_archive(filepath)
    elif excel_pattern.search(filepath):
      convert_excel_to_csv(filepath)
      
    return

  def convert_excel_to_csv(filepath):
    #
    # Implementation left as an exercise for the reader
    #
    return
  ```

### A Word of Caution
- Remember that premature optimization is the root of all evil.
- Resist the urge to split up functions based on edge cases that you may never encounter.


**[⬆ back to top](#list-of-contents)**

</br>

---
## References:
- https://towardsdatascience.com/the-single-responsibility-principle-in-python-d0ab0a681853