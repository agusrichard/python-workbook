class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        temp = ''
        for i in range(n+1):
            for j in range(i, n+1):
                subs = s[i:j]
                if subs  == subs[::-1] and len(subs) > len(temp):
                    temp = subs
                    
                    
        return temp
                    
import timeit

def longest_palindrome(s):
    n = len(s)
    if n < 2:
        return s

    start = 0
    max_length = 1
    for i in range(n):
        low = i - 1
        high = i + 1

        while low >= 0 and s[low] == s[i]:
            low -= 1
        
        while high < n and s[high] == s[i]:
            high += 1

        while (low >= 0 and high < n) and (s[low] == s[high]):
            low -= 1
            high += 1

        length = high - low - 1
        if max_length < length:
            max_length = length
            start = low + 1

    return s[start:start+max_length]


if __name__ == '__main__':
    # res = timeit.timeit(
    #     'longest_palindrome("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")',
    #     setup='from __main__ import longest_palindrome',
    #     number=1)
    # print(res)
    print(longest_palindrome('aba'))