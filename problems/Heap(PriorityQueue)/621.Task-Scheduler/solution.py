import heapq
from collections import defaultdict
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0

        tasks_left = defaultdict(int)
        for task in tasks:
            tasks_left[task] += 1

        h = [-count for count in tasks_left.values()]
        heapq.heapify(h)

        while h:
            count = 0
            task_counts = []
            i = 0

            while i < n + 1 and h:
                freq = -heapq.heappop(h)
                task_counts.append(freq - 1)

                count += 1
                i += 1

            for new_count in task_counts:
                if new_count > 0:
                    heapq.heappush(h, -new_count)

            cycles += n + 1 if h else count

        return cycles
