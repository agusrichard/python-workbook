def inputing_data(number_of_data):
    data = []
    for i in range(number_of_data):
        data.append(float(input(f"Data ke-{i+1}: ")))
    return data


def total(data):
    sum = 0
    for element in data:
        sum += element
    return sum

def average(data):
    return total(data)/len(data)

data = inputing_data(5)
print(data.reverse())
print(data.__getitem__(3))
print(data.__getitem__(3)==data[3])
print(data)
print(total(data))
print(average(data))

from math import sqrt

def is_prime(number):
    if number == 2:
        return True
    if (number < 2) or (number % 2 == 0):
        return False
    trial_factor = 3
    root = sqrt(number)
    while trial_factor <= root:
        if number % trial_factor == 0:
            return False
        trial_factor += 2
    return True

def prime_sequence(begin, end):
    for value in range(begin, end+1):
        if is_prime(value):
            yield value

def main():
    primes = list(prime_sequence(0,1000))
    print(primes)

if __name__ == '__main__':
    main()

lst = [98, 67, -1, -728, 873, 76, 54, 76 -81, 0]
print(lst)
lst1 = [x for x in lst if x >= 0 and x <= 0]
print(lst1)
lst2 = ['sekar', 2, 'arifa', 7, 9, 'saskia', 91, 69]
lst3 = [x for x in lst2 if type(x) is str]
print(lst3)
print([(x, x**2) for x in range(10)])
relations = [(x,y) for x in range(3) for y in range(3) if x != y]
print(relations)

n = int(input("Please enter a positive integer: "))
numbers = [(x,n//x) for x in range(1, n + 1) if (n%x) == 0]
print(numbers)

import math

n = int(input("Please enter a positive integer: "))
factors = [(x, n//x) for x in range(1,round(math.sqrt(n))) if (n%x) == 0]
print(factors)

L = [x for x in range(20) if x not in [12, 8, 3, 17]]
print(L)

#testing list comprehension with boolean value
P = [ x > 2 for x in [5, 1, 0, 7, 2, 7, 3]]
print(P)

primes = [p for p in range(2, 80) if not [x for x in range(2, p) if p % x == 0]]
print(primes)

#creating generator expression or generator comprehension instead of list comprehension
#if you just want to visit the sequence once, use generator comprehension!
for val in (2**x for x in range(10)):
    print(val, end=' ')

print()


#-----------------------------------------------------------------------------------------------------------------------
#dictionaries

d = {'Fred': 44, 'Ella': 39, 'Owen': 40, 'Zoe': 41}
print(d)

print(d.keys())
print(d.values())
print(type(d.keys()))
print(type(d.values()))

for k in d.keys():
    print(k, end=' ')
print()

for k in d:
    print((k), end=' ')
print()

for v in d.values():
    print(v, end=' ')
print()

for k,v in d.items():
    print(k, v)

print()
print()

names = ['Fred', 'Ella', 'Owen', 'Zoe']
numbers = [4174, 2287, 5003, 2012]
print(names)
print(numbers)
names_numbers = dict(zip(names, numbers))
print(names_numbers)

#------------------------------------------------------------------------------------------------------------------------
# keyword arguments

def f(**kwargs):
    a = kwargs['a']
    b = kwargs['b']
    c = kwargs['c']

    return 2*a*a + 3*b + c

def process(**kwargs):
    print(kwargs) #**kwargs will pack the whole argument into dictionary
    for key_arg, val_arg in kwargs.items():
        print(key_arg, '-->', val_arg)

def f_one(a,b,c):
    print('a =', a, 'b =', b, 'c = ', c)

f_one(1,2,3)
dic = {}
dic['b'] = 22
dic['c'] = 33
dic['a'] = 11
f_one(**dic)