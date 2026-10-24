class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i, coords in enumerate(points):
            x = coords[0]
            y = coords[1]
            d = x**2 + y**2
            entry = [-d, i]

            if len(h) < k:
                heapq.heappush(h, entry)
            else:
                heapq.heappushpop(h, entry)

        return [points[j] for _, j in h]