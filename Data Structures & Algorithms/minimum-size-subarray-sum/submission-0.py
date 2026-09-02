class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minwindow = float('inf')
        n = len(nums)
        left = 0
        total = 0

        if sum(nums) < target:
            return 0

        for right in range(n):
            
            total += nums[right]
            
            while total >= target:
                window = right - left + 1
                minwindow = min(window, minwindow)
                total -= nums[left]
                left += 1
            
            
        return minwindow
        



