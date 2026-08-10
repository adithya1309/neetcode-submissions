class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for previous in range(i):
                if nums[previous] < nums[i]:
                    dp[i] = max(dp[i], dp[previous] + 1)
        
        return max(dp)