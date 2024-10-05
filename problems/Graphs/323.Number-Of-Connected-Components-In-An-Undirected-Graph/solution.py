from typing import Dict, List, Set
from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(start: int, visited: Set[int], graph: Dict[int, List[int]]) -> None:
            visited.add(start)

            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs(neighbor, visited, graph)

        graph = defaultdict(list)
        for edge in edges:
            node1, node2 = edge
            graph[node1].append(node2)
            graph[node2].append(node1)
        for i in range(n):
            graph[i]

        visited = set()
        count = 0
        for node in graph:
            if node not in visited:
                count += 1
                dfs(node, visited, graph)

        return count
