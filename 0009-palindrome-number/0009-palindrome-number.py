class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindrome
        if x < 0:
            return False

        # Numbers ending in 0 are not palindrome,
        # except 0 itself
        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0

        while x > reversed_half:
            digit = x % 10
            x //= 10
            reversed_half = reversed_half * 10 + digit

        # Even digits: x == reversed_half
        # Odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10