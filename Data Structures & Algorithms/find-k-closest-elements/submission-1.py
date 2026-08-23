class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = k
        
        while right < n:
            if abs(x - arr[right]) < abs(x - arr[left]):
                left += 1
            right += 1
                
        
        return arr[left: left+k]

                

            