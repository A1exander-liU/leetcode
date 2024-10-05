from typing import Dict, List, Set
from collections import defaultdict


class Solution:
    """
        n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

        2
        |
        0 -- 1 -- 4
        |
        3


        n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

             4
             |
        0 -- 1 -- 2
             |    |
             - 3  -



        0 -- 1 -- 2 -- 3 -- 4

    DF can be used to detect a cycle in an undirected Graph.
    If we encounter a visited vertex again, then we say, there is a cycle.
    But there is a catch in this algorithm, we need to make sure that we do not consider
    every edge as a cycle because in an undirected graph, an edge from 1 to 2 also means
    an edge from 2 to 1. To handle this, we keep track of the parent node
    (the node from which we came to the current node) in the DFS traversal and
    ignore the parent node from the visited condition.


    0 -- 0
    """

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def hasCycle(
            start: int, parent: int, visited: Set[int], graph: Dict[int, List[int]]
        ) -> bool:
            visited.add(start)

            for neighbor in graph[start]:
                if neighbor in visited and neighbor != parent:
                    return True
                if neighbor not in visited:
                    if hasCycle(neighbor, start, visited, graph):
                        return True

            return False

        graph = defaultdict(list)
        degree = defaultdict(int)
        for edge in edges:
            node1, node2 = edge
            if node1 == node2:
                return False
            graph[node1].append(node2)
            graph[node2].append(node1)

            degree[node1] += 1
            degree[node2] += 1
        for i in range(n):
            graph[i]
            degree[i]

        count = 0
        visited = set()
        for node in graph:
            if count > 1:
                return False
            if node not in visited:
                count += 1
                if hasCycle(node, node, visited, graph):
                    return False

        return True
