import os

class WriteManager:
    def __init__(self, filename: str):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file: File = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit')
        if self.file:
            self.file.close()

with WriteManager('sekar.txt') as file:
    file.write('Sekardayu Hana Pradiani')