class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def rob_line(houses: List[int]) -> int:
            k = len(houses)
            dp = [0] * k
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, k):
                dp[i] = max(dp[i-1], houses[i] + dp[i-2])
            
            return dp[-1]
        
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))