class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0


        for num in sett:
            if (num - 1) not in sett:
                current = 1
                while (num + current) in sett:
                    current += 1
                longest = max(longest, current)
        
        return longest
