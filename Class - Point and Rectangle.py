import turtle

cat = turtle.Turtle()

class Point(object):
    """Represents a point in 2-D space"""

coordinate = Point()
coordinate.x = float(input("x: \n"))
coordinate.y = float(input("y: \n"))

class Rectangel(object):
    """Represents a rectangle in 2-D space
    attributes: width, height, and corner"""

box = Rectangel()
box.width = float(input("width: \n"))
box.height = float(input("height: \n"))
box.corner = coordinate

def print_point(spot):
    print('(%g,%g)' % (spot.x,spot.y))

def distance_between_points(coor):
    distance = ((coor.x**2)+(coor.y**2))**(1/2)
    return distance

def find_center(rect):
    center_point = Point()
    center_point.x = rect.corner.x + rect.width / 2.0
    center_point.y = rect.corner.y + rect.height / 2.0
    return center_point

def move_rectangle(rect,dx,dy):
    new_corner = Point()
    new_corner.x = rect.corner.x + dx
    new_corner.y = rect.corner.y + dy
    return 'width %g, height %g, corner (%g,%g)' % (rect.width,rect.height,new_corner.x,new_corner.y)

def drawing_rectangle(rect):
    for i in range(2):
        cat.forward(rect.width)
        cat.left(90)
        cat.forward(rect.height)
        cat.left(90)
    turtle.done()

drawing_rectangle(box)

