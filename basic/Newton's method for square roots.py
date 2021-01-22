a=float(input("> \n"))

def square_roots(a):
    x = a
    while True:
        y=(x + a/x)/2
        if x-y <= (1/1000000):
            break
        print(float(y))
        x=y

square_roots(a)
