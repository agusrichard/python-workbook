a=int(input())
b=int(input())
c=int(input())
d=int(input())

def countingproblem(a,b,c,d):
    a1=a
    b1=b
    c1=c
    d1=d
    while d1 >= 1:
        while c1 >= 1:
            while b1 >= 1:
                while a1 >= 1:
                    print(a1,b1,c1,d1)
                    a1=a1-1
                a1=a
                b1=b1-1
            a1=a
            b1=b
            c1=c1-1
        a1=a
        b1=b
        c1=c
        d1=d1-1

countingproblem(a,b,c,d)

