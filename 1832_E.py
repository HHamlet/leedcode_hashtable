"""Leedcode 1832. Check if the Sentence Is Pangram"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # letter = "abcdefghijklmnopqrstuvwxyz"
        # for el in letter:
        #     if el not in sentence:
        #         return False
        # return True

        if len(set(sentence)) == 26:
            return True
        else:
            return False


