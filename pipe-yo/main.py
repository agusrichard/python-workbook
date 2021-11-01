from pipe import select, where

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(my_list | where(lambda x: x % 2 == 0)))

updated_list = my_list \
    | select(lambda x: x * 3) \
    | where(lambda x: x % 2 == 0)

print(list(updated_list))