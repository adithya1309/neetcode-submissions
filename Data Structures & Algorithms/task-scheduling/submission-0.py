class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = [-c for c in Counter(tasks).values()]
        heapq.heapify(h)
        t = 0
        q = deque()

        while h or q:
            t += 1

            if q and q[0][1] == t:
                heapq.heappush(h, q.popleft()[0])

            if h:
                c = heapq.heappop(h) + 1
                if c < 0:
                    q.append((c, t + n + 1))
        
        return t