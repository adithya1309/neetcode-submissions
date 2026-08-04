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

        sum_of_s = 0
        for char in lists:
            sum_of_s += ord(char)
        sum_of_t = 0
        for char in listt:
            sum_of_t += ord(char)
        if sum_of_s == sum_of_t:
            return True
        else:
            return False



        
        

        