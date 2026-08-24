class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        

        while left < right:
            currentcapacity = left + (right - left) // 2
            currentdays = 1
            currentweight = 0

            for weight in weights:
                if (currentweight + weight) <= currentcapacity:
                    currentweight += weight
                else:
                    currentweight = weight
                    currentdays += 1
            
            if currentdays > days:
                left = currentcapacity + 1
            else:
                right = currentcapacity

        return left
                