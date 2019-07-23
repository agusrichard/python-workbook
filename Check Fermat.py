a = int(input("Masukan a: \n"))
b = int(input("Masukan b: \n"))
c = int(input("Masukan c: \n"))
n = int(input("Masukan n: \n"))

def inspectfermat(x1, x2, x3, x4):
    if ((x1 ** x4) + (x2 ** x4)) == (x3 ** x4):
        print(x1,x2,x3,x4)
        print("Holy Smokes, Fermat was wrong")
    else:
        print(x1,x2,x3,x4)
        print("That doesn't work")
    #inspecting fermat's last theorem

def checkfermat(a,b,c,n):
    a1=a
    b1=b
    c1=c
    d1=n
    while d1 >= 1:
        while c1 >= 1:
            while b1 >= 1:
                while a1 >= 1:
                    inspectfermat(a1,b1,c1,d1)
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
    #works like counting problem. using iteration, but i can't find a way with using recursion

checkfermat(a,b,c,n)
