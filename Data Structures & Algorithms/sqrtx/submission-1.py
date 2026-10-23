class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        a = 0

        while l <= r:
            m = l + (r - l) // 2
            p = m * m

            if p == x:
                return m
            elif p < x:
                l = m + 1
                a = m
            elif p > x:
                r = m - 1
        return a