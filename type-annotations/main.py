# The thing is type annotation does not affecting anything at runtime
# the purpose is for readibility of code
age: int = 23
print(age)
age = 'Twenty three'
print(age)

# :et's see the difference between using type annotations and without
def do_combine_1(x, y, times):
    return (x + y) *times

print(do_combine_1(1, 2, 3))
print(do_combine_1('hello', 'world', 3))

# Now change the previous code by using type annotations
def do_combine_2(x: str, y: str, times: int) -> str:
    return (x + y + ' ') * times

print(do_combine_2('sekar', 'dayu', 5))

# For primitive types, the tasks is particularly easy
# but we can have the same thing if we use non primitive types as such list, dict or set
from typing import List

def print_names(names: List[str]) -> None:
    for name in names:
        print(name)

print_names(['sekar', 'saskia', 'arifa'])
