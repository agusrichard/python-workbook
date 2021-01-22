import turtle

cat = turtle.Turtle()


# making triangle
def makingtriangle(x):
    cat.forward(x)
    for i in range(2):
        cat.left(120)
        cat.forward(x)


def makingsquare(x):
    cat.forward(x)
    for i in range(3):
        cat.left(90)
        cat.forward(x)


def makingheptagon(x):
    cat.forward(x)
    for i in range(5):
        cat.left(60)
        cat.forward(x)


def makingoctagon(x):
    cat.forward(x)
    for i in range(7):
        cat.left(45)
        cat.forward(x)


def makingdecagon(x):
    cat.forward(x)
    for i in range(11):
        cat.left(30)
        cat.forward(x)


# making polgygon
def makingpolygon(n, x):
    cat.forward(x)
    for i in range(n - 1):
        cat.left(360 / n)
        cat.forward(x)
    cat.left(360 / n)


def repeat_makingpolygon(a, x):
    b = 3
    while b != a:
        makingpolygon(b, x)
        b += 1


def circlesofpolygon(n,a,x):
    for i in range(n):
        repeat_makingpolygon(a,x)
        cat.right(360/n)


repeat_makingpolygon(100, 5)