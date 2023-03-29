"""Leedcode 771. Jewels and Stones"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {}
        cnt = 0
        for el in jewels:
            if el not in hashmap:
                hashmap[el] = 1

        for el in stones:
            if el in hashmap:
                cnt += 1
        return cnt


jewels = "z"
stones = "ZZ"
s = Solution
print(s.numJewelsInStones(s, jewels, stones))
