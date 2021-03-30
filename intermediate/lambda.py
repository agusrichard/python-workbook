addition = lambda x, y: x + y
print(addition(5, 2))

points = [(1, 2), (3, 4), (1, 2), (-1, -1)]
points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)

a = [1, 2, 3, 4, 5]
mapped = map(lambda x: x * 2, a)
print(list(mapped))

filtered = filter(lambda x: x < 3, a)
print(filtered)
filtered = [x for x in a if x%2 == 0]
print(filtered)

from functools import reduce
reduced = reduce(lambda x, y: x + y, a)
print(reduced)