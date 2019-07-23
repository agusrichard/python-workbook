matrix = [[100, 14, 8, 22, 71],
          [0, 243, 68, 1, 30],
          [90, 21, 7, 67, 112],
          [115, 200, 70, 150, 8]]

for row in matrix:
    for element in row:
        print('{:>4}'.format(element), end='')
    print()

print()

zero_one_matrix = [[0] * 5,
                   [1] * 5,
                   [0] * 5]
for row in zero_one_matrix:
    for element in row:
        print('{:>4}'.format(element), end='')
    print()

print()

a = [[0] * 4] * 3
a[1][2] = 5
print(a)

print()

b = [[0] * 4 for _ in range(4)]
b[1][3] = 5
for row in b:
    for element in row:
        print('{:>4}'.format(element), end='')
    print()

print()

c = [[0 for _ in range(4)] for _ in range(3)]
for row in c:
    for element in row:
        print('{:>4}'.format(element), end='')
    print()


# --------------------------------------------------------------------------
# We are learning about decorators

def div(a, b):
    print(a / b)


def smart_div(function):
    def inner(a, b):
        if a < b:
            a, b = b, a
        print('returning function')
        return function(a, b)

    print('returning inner')
    return inner


div1 = smart_div(div)

div1(2, 4)

# ---------------------------------------------------------------------------
# filter, map, reduce
from functools import reduce

numbers = list(range(10))

evens = list(filter(lambda x: x % 2 == 1, numbers))
print(evens)

doubles = list(map(lambda x: x * 2, numbers))
print(doubles)

sum = reduce(lambda x, y: x + y, numbers)
print(sum)


# -----------------------------------------------------------------------------------------------------------------------
##All about class and object... Based on something that we have learned in java
class Student:
    student_id = 0
    school = "Chicken Dinner"

    def __init__(self, name, major, laptop_brand):
        Student.student_id += 1
        self.name = name
        self.major = major
        self.student_id = Student.student_id
        self.laptop = Student.Laptop(laptop_brand)

    def __str__(self):
        return f"My name is {self.name} and majoring in {self.major}. The Identification number is {self.student_id}." \
            f" Nice to meet you!"

    @classmethod
    def get_school(self):
        return self.school

    @staticmethod
    def info():
        return "Sekardayu memang cantik sekali"

    class Laptop:

        def __init__(self, brand):
            self.brand = brand

        def __str__(self):
            return self.brand


sekar = Student("Sekardayu Hana Pradiani", "Actuarial Management", "HP")
saskia = Student("Saskia Nurul Azhima", "Accounting", "Macbook")
laptop1 = Student.Laptop("HP")
print(sekar)
print(laptop1)


# -----------------------------------------------------------------------------------------------------------------------
# tuples

def sum(*nums):
    print(nums)
    s = 0
    for num in nums:
        s += num
    return s


print(sum(1, 2, 3, 4, 5, 6, 7))
print(sum(1, 2, 3, 4, 5))


def f(a, b, c, d):
    print(a, b, c, d)


args = (10, 20, 30, 40)
f(*args)

a = 1, 2, 3, 4, 5, 6, 7
print(a)
x, y, *rest = a
print(x)
print(y)
print(rest)

# -----------------------------------------------------------------------------------------------------------------------
# dictionaries as counter

text = input("Apa yang ingin kamu katakan pada sekar? \n")

text = text.upper()
text_list = text.split()
counters = {}
for word in text_list:
    if word not in counters:
        counters[word] = 1
    else:
        counters[word] += 1
for word, count in counters.items():
    print(word, count)

s = " 85, 54 , 13, 17, 44 ,31, 80, 35, 30, 54, 78 "
print(s)
int_list = [int(x.strip()) for x in s.split(",")]
print(int_list)

#-----------------------------------------------------------------------------------------------------------------------
#Sets

S = {10, 3, 7, 2, 3, 1} #it is unordered and the repetition elements are eleminated
print(type(S))
print(S)
print("----------------------------------")

L = [10, 13, 10, 5, 6, 13, 2, 10, 5]
S = set(L)
print(L)
print(S)
print("----------------------------------")

# empty dictionary represented by {} but empty set represented by set()

S = {2, 5, 7, 8, 9, 12}
T = {1, 5, 6, 7, 11, 12}

print(S | T) #represent Union
print(S & T) #represent Intersection
print(S - T) #represent Set difference
print(S ^ T) #represent Symmetric difference
print(S <= T) #represent Subset

#trying to make set comprehension
A = {x**2 for x in range(10)}
print(A)

# coding=utf-8
# -----------------------------------------------------------------------------------------------------------------------
# 11.9 Set Quantification with all and any

S = {1, 2, 3, 4, 5, 6, 7, 8} # for all x element of S, such that x is greater than zero
print(S)

# Universal Quantification

bool_list = [x > 0 for x in S]
print(bool_list)
print(all(bool_list))  # function will return True if all the elements in a list
tup = (x > 0 for x in S)
print(tup)
print(type(tup))
print(all(tup))  # this is the way python represents universal quantification(∀x∈S)(x > 0).

print("----------------------------", end="\n\n")


# Existential Quantification

print(any(x > 0 for x in S)) # python way to represent (∃x∈S)(x>0).

print("----------------------------", end="\n\n")


#Testing the time performance between sets and lists

size = 1000

S = {x**2 for x in range(size)}
L = [x**2 for x in range(size)]

print('Set:', type(S), "List:", type(L))


from time import perf_counter

search_size = 1000000

# time list access
start_time = perf_counter()
for i in range(search_size):
    if i in L:
        pass
stop_time = perf_counter()
print('List elapsed:', stop_time - start_time)

# time set access
start_time = perf_counter()
for i in range(search_size):
    if i in S:
        pass
stop_time = perf_counter()
print('Set elapsed:', stop_time - start_time)

# ----------------------------------------------------------------------------------------------------------------------
# 11.10 Enumerating the elements of data structures
# Enumeration sometimes more effective
# Enumeration return enumerate object that pair key and value
# for any kind of data structures

lst = [10, 20, 30, 40, 50]
t = 100, 200, 300, 400, 500
d = {"A": 4, "B": 18, "C": 0, "D": 3}
s = {1000, 2000, 3000, 4000, 5000}
print(lst)
print(t)
print(d)
print(s)

for x in enumerate(lst):
    print(x, end=" ")
print()
for x in enumerate(t):
    print(x, end=" ")
print()
for x in enumerate(d):
    print(x, end=" ")
print()
for x in enumerate(s):
    print(x, end=" ")
print()

def gen(n):
    """ Generate n, n - 2, n - 3, ..., 0. """
    for i in range(n, -1, -2):
        yield i

for x in enumerate(gen(20)):
    print(x, end=" ")
print()


