from re import sub
from typing import List


class DS:
    """
    Index `i` is node `i`
    node subsets[i] is parent of node `i`
    representative of set: when subsets[i] == i

    start
    Value: 0 1 2 3 4 5
    Index: 0 1 2 3 4 5

    union(1,3)
    Value: 0 1 2 1 4 5
    Index: 0 1 2 3 4 5 update index 3 to point to 1

    union(2,3)
    Value: 0 1 3 1 4 5
    Index: 0 1 2 3 4 5 update index 2 to point to 3

    find what subset `x` belongs to?
    - if subsets[x] == `x`, this is root (representative of entire set)
    - otherwise recursively find susbets[x]

    find(3)
    subsets[3] = 2; 3 != 2 so keep going
    subsets[2] = 1; 2 != 1 so keep going
    subsets[1] = 1; 1 == 1 so 1 is root
    """

    def __init__(self, n: int) -> None:
        self.subsets = []
        self.ranks = []

        for i in range(n + 1):
            self.subsets.append(i)
            self.ranks.append(0)

    def find(self, x: int) -> int:
        if x == self.subsets[x]:
            return x

        root = self.find(self.subsets[x])
        # update its parent before returning to prevent traversing all over again when calling `find(4) again`
        self.subsets[x] = root
        return root

    def union(self, x: int, y: int) -> bool:
        subsetX = self.find(x)
        subsetY = self.find(y)
        if subsetX == subsetY:
            return False

        # rank store height of: 1 <-  2 <- 3
        # always put subset with smaller height under bigger height one
        if self.ranks[subsetX] < self.ranks[subsetY]:
            self.subsets[subsetX] = subsetY
        elif self.ranks[subsetY] < self.ranks[subsetX]:
            self.subsets[subsetY] = subsetX
        else:
            self.subsets[subsetX] = subsetY
            self.ranks[subsetY] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DS(len(edges))

        for edge in edges:
            if not ds.union(edge[0], edge[1]):
                return edge

        return []


cases = [
    [[1, 2], [1, 3], [2, 3]],
    [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
    [[1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [5, 6]],
]

s = Solution()
print("Result:", s.findRedundantConnection(cases[2]))
