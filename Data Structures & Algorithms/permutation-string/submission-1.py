class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        n = len(s2)
        m = len(s1)
        for s in s1:
            seen[s] = seen.get(s, 0) + 1
        
        freq = {}
        left = 0
        for right in range(n):
            freq[s2[right]] = freq.get(s2[right], 0) + 1
            w = right - left + 1
            while w > m:
                freq[s2[left]] -= 1
                if freq [s2[left]] == 0:
                    del freq[s2[left]]
                left += 1
                w = right - left + 1
            if freq == seen:
                return True
        return False
            
        
