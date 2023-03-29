import collections

""" Leedcode 2423. Remove Letter To Equalize Frequency"""


class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            c = collections.Counter(word)
            char = word[i]
            c[char] -= 1
            if c[char] == 0:
                del [c[char]]
            if len(set(c.values())) == 1:
                return True
        return False


word = "abcc"
s = Solution
print(s.equalFrequency(s, word))
