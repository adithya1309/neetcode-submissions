class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        minfrequency = n/3
        hashmap = {}
        result = []

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for number, frequency in hashmap.items():
            if frequency > minfrequency:
                result.append(number)
        
        return result

