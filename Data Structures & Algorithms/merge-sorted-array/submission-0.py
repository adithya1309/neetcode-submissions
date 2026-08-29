class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m
        p2 = 0

        while p2 < n:
            if nums1[p1] == 0:
                nums1[p1] = nums2[p2]
                p1 += 1
                p2 += 1
            
        return nums1.sort()