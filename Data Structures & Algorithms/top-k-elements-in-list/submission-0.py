class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 0
        sortedDict = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True)[:k])
        return list(sortedDict)


