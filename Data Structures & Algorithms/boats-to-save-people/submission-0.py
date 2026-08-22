class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left = 0
        boats = 0
        right = n - 1
  

        while left <= right:
            currentweight = people[left] + people[right]
            if currentweight <= limit:
                right -= 1
                left += 1
                boats +=1
            else:
                right -= 1
                boats += 1
            
        return boats


