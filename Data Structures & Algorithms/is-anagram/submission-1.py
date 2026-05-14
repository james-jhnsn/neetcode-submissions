class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = {}

        word_2 = {}

        for l in s:
            word_1[l] = word_1.get(l, 0) + 1

        for l in t:
            word_2[l] = word_2.get(l, 0) + 1

        if word_1 == word_2:
            return True

        return False
