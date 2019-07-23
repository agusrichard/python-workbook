x = input("Masukan besar langkah yang diinginkan: \n")
n = input("Banyaknya langkah yang akan dilewati: \n")
rep = input("Pengulangan yang diinginkan: \n")

import turtle
import random

cat = turtle.Turtle()
list1 = [0,1,2,3]
list2 = [0,1,2]

def random_walk_1(length, how_much):
    """This function takes parameter length as the length of the turtle; how_much as the number of process that will occur"""

    cat.left(90)    #making cat face upward
    cat.speed(10)
    for i in range(how_much):
        if random.choice(list1) == 0:
            cat.forward(length)
        elif random.choice(list1) == 1:
            cat.backward(length)
        elif random.choice(list1) == 2:
            cat.left(random.randint(0,360))
        elif random.choice(list1) == 3:
            cat.right(random.randint(0,360))
    turtle.done()

def random_walk_2(length, how_much,repetition):
    """This function takes turtle move and back to (0,0), and do the same process again"""

    cat.left(90)
    cat.speed(10)
    for a in range(repetition):
        for i in range(how_much):
            if random.choice(list2) == 0:
                cat.forward(length)
            elif random.choice(list2) == 1:
                cat.right(random.randint(0,90))
            else:
                cat.left(random.randint(0,90))
        cat.pu()
        cat.home()
        cat.pd()
    turtle.done()

random_walk_2(int(x),int(n),int(rep))




