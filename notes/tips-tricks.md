# Tips and Tricks in Python

</br>

## List of Contents:
### 1. [5 Powerful Python One-Liners You Should Know](#content-1)


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

## References:
- https://levelup.gitconnected.com/5-powerful-python-one-liners-you-should-know-469b9c4737c7