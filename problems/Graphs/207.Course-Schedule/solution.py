from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, prerequisites: List[List[int]]) -> bool:
        degree = defaultdict(int)
        graph = defaultdict(list)

        for prerequisite in prerequisites:
            dst, src = prerequisite
            degree[dst] += 1
            degree[src]

            graph[src].append(dst)
            graph[dst]

        candidates = deque([v for v in graph if degree[v] == 0])
        while len(candidates) > 0:
            v = candidates.popleft()

            for neighbor in graph[v]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    candidates.append(neighbor)

            del graph[v]

        return not graph
