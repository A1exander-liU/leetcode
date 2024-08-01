import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.all_tweets = []
        self.followers = defaultdict(set)

    def _updateFeed(self, userId) -> List[int]:
        feed = []
        i = len(self.all_tweets) - 1
        while i >= 0 and len(feed) < 10:
            if (
                self.all_tweets[i][0] == userId
                or self.all_tweets[i][0] in self.followers[userId]
            ):
                feed.append(self.all_tweets[i][1])
            i -= 1

        return feed

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.all_tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        return self._updateFeed(userId)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


def findMedian(min_heap, max_heap) -> float:
    min_store = []
    max_store = []

    n = len(min_heap)
    if n % 2 == 1:
        pop_count = n // 2
    else:
        pop_count = n // 2 - 1

    for i in range(pop_count):
        min_store.append(heapq.heappop(min_heap))
        max_store.append(heapq.heappop(max_heap))

    mid = (min_heap[0] + -max_heap[0]) / 2

    for val in min_store:
        heapq.heappush(min_heap, val)
    for val in max_store:
        heapq.heappush(max_heap, val)

    return mid


min = []
max = []

# 2 5 6 6 10 = 5,6
"""
        0
     5    2
  10   6 6

        10
     6      2
  6    5  0
"""

nums = [6, 10, 2, 6, 5, 0]


for num in nums:
    heapq.heappush(min, num)
    heapq.heappush(max, -num)


pop_count = len(min) // 2 if len(min) % 2 == 1 else len(min) // 2 - 1
odd = len(min) % 2 == 1

for i in range(pop_count):
    heapq.heappop(min)


if odd:
    print(heapq.heappop(min))
else:
    print(heapq.heappop(min), heapq.heappop(min))
