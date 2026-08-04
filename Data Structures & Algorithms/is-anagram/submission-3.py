class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lists = list(s)
        lists.sort()
        listt = list(t)
        listt.sort()
        if listt != lists:
            return False
        else:
            return True

       