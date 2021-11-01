# Write Clean Python Code Using Pipes

## Motivation
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

