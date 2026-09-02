class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            product = mid * mid

            if product == x:
                return mid
            elif product < x:
                left = mid + 1
                ans = mid
            elif product > x:
                right = mid - 1

        return ans