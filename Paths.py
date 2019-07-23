import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname,name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


walk('C:\\Users\\Agus Richard\\PycharmProjects\\Project1')