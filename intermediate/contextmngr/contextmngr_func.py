from contextlib import contextmanager

@contextmanager
def write_file(filename: str):
    file = open(filename, 'w')
    try:
        yield file
    finally:
        file.close()


with write_file('saskia.txt') as file:
    file.write('Saskia Nurul Azhima')