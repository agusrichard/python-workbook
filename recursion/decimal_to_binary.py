

from unittest import TestCase, main


def decimal_to_binary(num: int) -> str:
    if num == 0:
        return '0'

    if num == 1:
        return '1'
    

    return decimal_to_binary(num // 2) + str(num % 2)

class TestDecimalToBinary(TestCase):
    def test_zero(self):
        actual = decimal_to_binary(0)
        expected = '0'
        self.assertEqual(actual, expected)

    def test_small_values(self):
        self.assertEqual(decimal_to_binary(1), '1')
        self.assertEqual(decimal_to_binary(2), '10')
        self.assertEqual(decimal_to_binary(3), '11')
        self.assertEqual(decimal_to_binary(4), '100')

    def test_compare_with_bin(self):
        for i in range(100):
            self.assertEqual(decimal_to_binary(i), bin(i)[2:])

if __name__ == '__main__':
    main(verbosity=2)