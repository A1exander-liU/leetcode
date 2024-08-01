from typing import Optional, Dict
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        def bfs(start: Optional["Node"]) -> Dict[int, "Node"]:
            visited = set([start])
            q = deque([start])

            nodeMap = {}

            while len(q) > 0:
                node = q.popleft()

                if node.val not in nodeMap:
                    clonedNode = Node(val=node.val, neighbors=[])
                    nodeMap[node.val] = clonedNode

                for neighbor in node.neighbors:
                    if neighbor.val not in nodeMap:
                        clonedNeighborNode = Node(val=neighbor.val, neighbors=[])
                        nodeMap[neighbor.val] = clonedNeighborNode

                    nodeMap[node.val].neighbors.append(nodeMap[neighbor.val])

                    if neighbor in visited:
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)

            return nodeMap

        if not node:
            return None

        nodeMap = bfs(node)
        return nodeMap[node.val]
