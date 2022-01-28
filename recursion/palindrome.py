from typing import Iterable
from unittest import TestCase, main


def palindrome(iters: Iterable) -> bool:
    return palindrome_helper(iters, 0, len(iters)-1)

def palindrome_helper(iters: Iterable, start: int, end: int) -> bool:
    if len(iters) == 0:
        return True

    if start >= end:
        return True

    if iters[start] != iters[end]:
        return False

    return palindrome_helper(iters, start+1, end-1)

class TestPalindrome(TestCase):
    def test_empty_list(self):
        actual = palindrome([])
        expected = True
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        actual = palindrome('')
        expected = True
        self.assertEqual(actual, expected)

    def test_palindrome_string(self):
        actual = palindrome('racecar')
        expected = True
        self.assertEqual(actual, expected)

    def test_palindrome_list(self):
        actual = palindrome([1,2,3,3,2,1])
        expected = True
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    main(verbosity=2)