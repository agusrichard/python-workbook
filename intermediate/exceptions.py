# with open('sometext.txt', 'r') as f:
#     print(f)
# assert 5 == 7, '5 is not the same as 7'

try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('Everything is fine')
finally:
    print('Cleaning up...')


class ValueTooHighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value