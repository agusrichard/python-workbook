import unittest

from main import get_cwd, Calculator, Random

class TestMock(unittest.TestCase):
    def test_using_context_manager(self):
        with unittest.mock.patch('main.os') as mocked_os:
            get_cwd()
            mocked_os.getcwd.assert_called_once()

    @unittest.mock.patch('main.os')
    def test_using_decorator(self, mocked_os):
        get_cwd()
        mocked_os.getcwd.assert_called_once()

    def test_using_context_manager_return_value(self):
        with unittest.mock.patch('main.os.getcwd', return_value='testing') as mocked_os:
            assert get_cwd() == 'testing'
            mocked_os.assert_called()

    @unittest.mock.patch('main.os.getcwd', return_value='testing')
    def test_using_decorator_return_value(self, mocked_os):
        assert get_cwd() == 'testing'
        mocked_os.assert_called()

    @unittest.mock.patch('main.Random')
    def test_Calculator_class(self, MockedRandom):
        MockedRandom.return_value.give_integer.return_value = 1
        calc = Calculator()
        assert calc.double() == 2
        MockedRandom.assert_called()

    @unittest.mock.patch('main.Random')
    def test_Calculator_class_full_fleged(self, MockedRandom):
        Calculator(0, 100)
        MockedRandom.assert_called_once_with(0, 100)

    @unittest.mock.patch.object(Random, 'give_integer', return_value=1)
    def test_Calculator_class_attributes_and_double(self, MockedRandom):
        calc = Calculator(0, 100)
        self.assertEqual(calc.double(), 2)
        self.assertEqual(calc.r.start, 0)
        self.assertEqual(calc.r.end, 100)



if __name__ == '__main__':
    unittest.main()