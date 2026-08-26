class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 1. Ignore leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Convert digits
        num = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Check overflow
            if num > (2**31 - 1 - digit) // 10:
                if sign == 1:
                    return 2**31 - 1
                else:
                    return -2**31

            num = num * 10 + digit
            i += 1

        return sign * num