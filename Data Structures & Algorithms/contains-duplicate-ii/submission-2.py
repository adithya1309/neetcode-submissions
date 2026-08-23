class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for index, number in enumerate(nums):
            if number in hashmap:
                if abs(index - hashmap[number]) <= k:
                    return True
                elif abs(index - hashmap[number]) > k:
                    hashmap[number] = index
            else:
                hashmap[number] = index
        
        return False