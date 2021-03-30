from itertools import product, permutations, combinations, combinations_with_replacement, \
    groupby

# product (cartesian product)
a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat=2)
print(list(prod))
print()


# permutations
a = [1, 2, 3]
perm = permutations(a)
perm1 = permutations(a, 2)
print(list(perm))
print(list(perm1))
print()

# combinations
a = [7, 8, 9]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
print()

# accumulate
# a = [1, 2, 3, 4, 5]
# acc = accumulate(a)
# print(acc)

# groupby
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group_obj = groupby(nums, key=lambda x: x <= 5)
for key, val in group_obj:
    print(key, list(val))
print()

from itertools import count, cycle, repeat
# count will create a infinite counting numbers
# cycle will infinitely cycling an iterable object
# repeat will infinitely some object