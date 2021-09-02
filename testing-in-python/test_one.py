from unittest import TestCase

def multiply(a: int, b: int) -> int:
    if a < 0 or b < b:
        raise ValueError('Must be greater than zero')
    return a * b

class TestOne(TestCase):
    def setUp(self) -> None:
        print('Setup the test')

    def tearDown(self) -> None:
        print('Teardown the test')

    def test_multiple(self):
        expected = 10
        result = multiply(2, 5)
        self.assertEqual(expected, result)

    def test_raise_value_error(self):
        with self.assertRaises(ValueError) as exception_context:
            multiply(-5, -2)
        self.assertEqual(str(exception_context.exception), 'Must be greater than zero')