class Solution:
    def shortestPalindrome(self, s):
        rev = s[::-1]

        temp = s + "#" + rev

        lps = [0] * len(temp)

        j = 0
        for i in range(1, len(temp)):
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]

            if temp[i] == temp[j]:
                j += 1
                lps[i] = j

        longest_pal_prefix = lps[-1]

        return rev[:len(s) - longest_pal_prefix] + s