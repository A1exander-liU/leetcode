from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        start = 0

        q = deque()

        for end in range(k):
            while q and q[-1] < nums[end]:
                q.pop()
            q.append(nums[end])

        result.append(q[0])
        for end in range(k, len(nums)):

            if q[0] == nums[end - k]:
                q.popleft()

            while q and q[-1] < nums[end]:
                q.pop()
            q.append(nums[end])

            result.append(q[0])


        return result