class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for i in range(n):
            asteroid = asteroids[i]
            alive = True

            while alive == True and stack and stack[-1] > 0 and asteroid < 0:
                latest = stack[-1]
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    alive = False
                elif stack[-1] > abs(asteroid):
                    alive = False
            if alive:
                stack.append(asteroid)
        
        return stack