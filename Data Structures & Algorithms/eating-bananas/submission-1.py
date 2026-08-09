class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right  = max(piles)
        answer = right

        while left <= right:
            mid =  left + (right - left) // 2
            
            totaltime = 0
            for p in piles:
                totaltime += math.ceil(p / mid)
            
            if totaltime <= h:
                answer = mid
                right = mid - 1
            elif totaltime > h:
                left = mid + 1
            
        return answer

                    