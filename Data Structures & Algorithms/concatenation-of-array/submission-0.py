class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = nums.copy()
        for num in nums2:
            nums.append(num)

        return nums