mylist = [1, 2, 3, 4, 5]

# List indexing
print(mylist[0])
print(mylist[:2])
print(mylist[2:])
print(mylist[:])

# In statement
print(9 in mylist)
if 9 in mylist:
    print('There is nine in mylist')
else:
    print('There is no nine in here')

# len function, how many elements inside a list
print(len(mylist))

# append method
mylist.append('sekar')
print(mylist)

# insert method (you can insert in specific index)
mylist.insert(0, 'saskia')
print(mylist)

# remove item inside a list
sekar = mylist.pop(len(mylist)-1)
saskia =  mylist.pop(0)
print(sekar, saskia)
print(mylist)

# clearing the list
mylist.clear()
print(mylist)

# reverse method
mylist = ['sekar', 'saskia', 'arifa']
mylist.reverse()
print(mylist)

# sort method
mylist = [3, 0, 1, -1, 4, 0, -1]
mylist.sort()
print(mylist)

# sorted function
new_list = sorted(mylist)
print(new_list)

# duplicating item in a list
mylist = [1] * 10
print(mylist)

# concatenating list
list1 = [1, 2, 3]
list2 = [1, 2, 3]
new_list = list1 + list2
print(new_list)

# Sort and copy in a different way
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = mylist[:]
mylist[0] = 'sekar'
print(mylist)
print(new_list)
print(new_list[::-1])
print([*mylist])

# List comprehension
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubes = [i**3 for i in mylist]
print(mylist)
print(cubes)