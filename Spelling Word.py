letter = str(input(">"))

def print_each_letter(x):
    a = 0
    while a <= (len(x)-1):
        print(x[a])
        a+=1

for char in letter:
    print(char)


def print_backwards(x):
    a=len(x)-1
    while a>=0:
        print(x[a])
        a=a-1

