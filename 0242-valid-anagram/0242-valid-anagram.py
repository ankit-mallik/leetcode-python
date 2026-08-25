class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()
        count = 0

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in letters:
                return False
            elif letters[t[i]] <= 0:
                return False
            letters[t[i]] -= 1
        return True