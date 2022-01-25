import random
import string
from unittest import TestCase, main

def reverse_string(x: str):
    if len(x) == 0:
        return ''

    if len(x) == 1:
        return x[0]

    return reverse_string(x[1:]) + x[0]


class TestReverseString(TestCase):
    def test_empty_string(self):
        actual = reverse_string('')
        expected = ''
        self.assertEqual(actual, expected)

    def test_single_character(self):
        actual = reverse_string('a')
        expected = 'a'
        self.assertEqual(actual, expected)

    def test_word_hello(self):
        actual = reverse_string('hello')
        expected = 'olleh'
        self.assertEqual(actual, expected)

    def test_random_word(self):
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) 
        actual = reverse_string(random_string)
        expected = random_string[::-1]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    # print(reverse_string('Sekar'))
    main(verbosity=2)