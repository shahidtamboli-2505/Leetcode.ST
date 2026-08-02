class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        valid = set()
        ans = ""

        for word in words:
            if len(word) == 1 or word[:-1] in valid:
                valid.add(word)
                if len(word) > len(ans):
                    ans = word

        return ans