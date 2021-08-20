# Tips and Tricks in Python

</br>

## List of Contents:
### 1. [5 Powerful Python One-Liners You Should Know](#content-1)
### 2. [11 Python Tricks to Boost Your Python Skills Significantly](#content-2)
### 3. [3 Useful Python f-string Tricks You Probably Don’t Know](#content-3)


</br>

---

## Contents:

## [5 Powerful Python One-Liners You Should Know](https://levelup.gitconnected.com/5-powerful-python-one-liners-you-should-know-469b9c4737c7) <span id="content-1"></span>

### 1- Typecasting of all items in a list
- Example 1:
  ```python
  >>> list(map(int, ['1', '2', '3']))

  # Output
  [1, 2, 3]
  ```
- Example 2:
  ```python
  >>> list(map(float, ['1', 2, '3.0', 4.0, '5', 6]))

  # Output
  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
  ```

### 2- Sum of digits of an integer
- This example is a bit weird!
- Example:
  ```python
  sum_of_digits = lambda x: sum(map(int, str(x)))
  print(sum_of_digits(1789))

  # Output
  25
  ```

### 3- Flat a list that contains sublists
- The old way:
  ```python
  flattened_list = []
  for sublist in l:
      for item in sublist:
          flattened_list.append(item)
  ```
- The one-liner:
  ```python
  >>> l = [[1, 2, 3], [4, 5], [6], [7, 8], [9]]
  >>> flattened_list = [item for sublist in l for item in sublist]
  >>> print(flattened_list)

  # Output
  [1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

### 4- Transpose of a Matrix
- Example:
  ```python
  >>> A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  >>> transpose_A = [list(i) for i in zip(*A)]
  ```


### 5- Swap keys and values in a dictionary
- Example:
  ```python
  >>> staff = {'Data Scientist': 'John', 'Django Developer': 'Jane'}
  >>> staff = {i:j for j, i in staff.items()}
  ```


**[⬆ back to top](#list-of-contents)**

</br>

---

## [11 Python Tricks to Boost Your Python Skills Significantly](https://python.plainenglish.io/11-python-tricks-to-boost-your-python-skills-significantly-1a5221dfa5c7) <span id="content-2"></span>

### 1- Remove repeated items from a list
- Example:
  ```python
  >>> numbers = [1, 2, 2, 3, 3, 3]
  >>> print(list(set(numbers)))
  ```

### 2- Zip Your Data
- Example:
  ```python
  >>> names = list(zip((1, 2), ['Anna', 'Alice']))
  >>> print(names)
  ```

### 3- Reverse Lists
- Example:
  ```python
  >>> numbers = [1, 2, 3, 4, 5]
  >>> print(numbers[::-1])
  ```

### 4- Count all occurrences
- Example:
  ```python
  >>> from collections import Counter
  >>> numbers = [1, 1, 1, 2, 1, 4, 4, 4, 3, 6]
  >>> c = Counter(numbers)
  >>> print(c)

  # Output, returned a Counter object
  Counter({1: 4, 4: 3, 2: 1, 3: 1, 6: 1})
  ```

### 5- Check Your Python Version
- Example:
  ```python
  >>> import sys
  >>> print(sys.version_info)

  sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)
  ```

### 6- Print your data with separators:
- Example:
  ```python
  >>> username = "user"
  >>> host = "mail.com"
  >>> print(username, host,sep="@")

  # Output
  user@mail.com
  ```

### 7- Swap dictionary key & values:
- Example:
  ```python
  >>> mydict= {1: 11, 2: 22, 3: 33}
  >>> mydict = {i: j for j, i in mydict.items()}
  >>> print(mydict)

  # Output
  {11: 1, 22: 2, 33: 3}
  ```

### 8- Get indexes of all letters from a string
- Example:
  ```python
  >>> s = ”Python”
  >>> e = enumerate(s)
  >>> print(list(e))

  # Output
  [(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
  ```

### 9- Check if objects are the same with is & not is
- To check if two things refer to the same thing, use `is` operator
- Example:
  ```python
  >>> t1 = ["Africa"]
  >>> t2 = ["Africa"]
  >>> t3 = t2
  >>> print(t1 is t2)
  >>> print(t1 is t3)
  >>> print(t1 is not t2)

  # Output
  False
  False
  True
  ```

### 10- Concatenate tuples
- Example:
  ```python
  >>> colors = ('blue', 'red') + ('yellow', 'green')
  >>> print(colors)

  # Output
  ('blue', 'red', 'yellow', 'green')
  ```

### 11- Use return instead of return None
- In Python, if return value of a function is not specified, the function returns None by default.
- Example:
  ```python
  >>> def double(n):
  ...     print(n * 2)
  >>> double(5)
  >>> print(type(double(5)))
  ```


**[⬆ back to top](#list-of-contents)**

</br>

---

## [3 Useful Python f-string Tricks You Probably Don’t Know](https://betterprogramming.pub/3-useful-python-f-string-tricks-you-probably-dont-know-f908f7ed6cf5) <span id="content-3"></span>

### Introduction
- How we do it the old way and new way:
  ![How we do it the old way and new way](https://miro.medium.com/max/700/1*kkgkA8RkrR2PzuvoDYC7pw.png)
- Simply prefix your string with an f or F and then followed by single, double, or even triple quotes to create your string, e.g., f"Hello, Python!".


### 1. F-string for Debugging
- Simple huh?
  ```python
  viewer = "🐊"
  owner = "🐼"
  editor = "🐓"

  print(viewer)
  print(owner)
  print(editor)
  ```
- Sometimes we are confused about which variable is printed. This how we can improve debugging process:
  ```python
  print(f"{viewer=}")
  print(f"{owner=}")
  print(f"{editor=}")

  # Stdout:

  # viewer = "🐊"
  # owner = "🐼"
  # editor = "🐓"
  ```
- Furthermore, using f-string this way preserves whitespaces, which can be helpful during our debugging process when we are in the midst of looking at confusing terminal logs.
  ```python
  print(f"{viewer=     }")
  print(f"{owner     =}")
  print(f"{editor     =      }")

  # Stdout:

  # viewer=     '🐊'
  # owner     ='🐼'
  # editor     =      '🐓'
  ```

### 2. String Formatting
- How to format float:
  ```python
  # The "old" ways of updating float to 2 decimal places
  float_variable = 3.141592653589793

  print("%.2f" % float_variable)
  print("{:.2f}".format(float_variable))

  # Stdout:

  # 3.14
  # 3.14

  # The new way with f-string
  float_variable = 3.141592653589793

  print(f"{float_variable:.2f}")

  # Stdout:
  # 3.14
  ```
- Formatting currency:
  ```python
  money = 3_142_671.76 # 💡 This is the same as 3142671.76

  print(f"${money:,.2f}")

  # Stdout:
  # $3,142,671.76
  ```
- Formatting datetime:
  ```python
  from datetime import datetime


  now = datetime.now()

  # The usual way
  formatted_datetime_now = now.strftime('%d-%B-%Y')
  print(formatted_datetime_now)

  # F-string way
  formatted_datetime_now = f"{now:%d-%B-%Y}"
  print(formatted_datetime_now)

  # Stdout
  # 05-July-2021
  ```
- Padding your int variables with leading zeroes or whitespaces
  ```python
  # Output length of 20, and pad the rest with zeroes

  int_variable = 1_234_567
  print(f'{int_variable:020}')

  # Stdout
  # 00000000000001234567


  # Output length of 24, and pad the rest with zeroes
  int_variable = 30
  print(f'{int_variable:024}')

  # Stdout
  # 000000000000000000000030
  ```
  ```python
  # Output length of 10, and pad the rest with leading whitesplace
  int_variable = 20_21
  print(f'{int_variable:10d}')

  # Stdout
  # '      2021'


  # Output length of 5, and pad the rest with leading whitesplace
  print(f"{int_variable:5d}")

  # Stdout
  # ' 2021'
  ```


### Conversion
- Convert your string to ASCII representation
  ```python
  owl = '🦉'
  print(f'{owl!a}')

  # Stdout
  # '\U0001f989'
  ```
- A repr() alternative with f-string
  ```python
  from datetime import datetime


  now = datetime.now()

  # Using repr()
  print(repr(now))


  # F-string way
  print(f'{now!r}')

  # Stdout
  # datetime.datetime(2021, 7, 5, 13, 2, 34, 672383)

  repr(now) == f'{now!r}'
  # True
  ```



**[⬆ back to top](#list-of-contents)**

</br>

---

## References:
- https://levelup.gitconnected.com/5-powerful-python-one-liners-you-should-know-469b9c4737c7
- https://python.plainenglish.io/11-python-tricks-to-boost-your-python-skills-significantly-1a5221dfa5c7
- https://betterprogramming.pub/3-useful-python-f-string-tricks-you-probably-dont-know-f908f7ed6cf5