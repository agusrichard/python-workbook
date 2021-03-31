def square_numbers(n):
    for i in range(n):
        yield i**2

g = square_numbers(1000)
g = (i**2 for i in range(1000) if i%2 == 0)
l = [i**2 for i in range(1000) if i%2 == 0]
for i in g:
    print(i)