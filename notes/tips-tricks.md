# Tips and Tricks in Python

</br>

## List of Contents:
### 1. [5 Powerful Python One-Liners You Should Know](#content-1)
### 2. [11 Python Tricks to Boost Your Python Skills Significantly](#content-2)


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
## References:
- https://levelup.gitconnected.com/5-powerful-python-one-liners-you-should-know-469b9c4737c7