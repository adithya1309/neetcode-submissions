class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        n = len(position)
        times = []
        for p, s in cars:
            d = target - p
            time = d / s
            times.append(time)
            if len(times) >= 2:
                if times[-1] <= times[-2]:
                    times.pop()
        return len(times)
