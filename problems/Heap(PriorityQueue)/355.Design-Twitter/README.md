# Problem
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the `Twitter` class:

- `Twitter()` Initializes your twitter object.
- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID `tweetId` by the user `userId`. Each call to this function will be made with a unique tweetId.
- `List<Integer> getNewsFeed(int userId)` Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- `void follow(int followerId, int followeeId)` The user with ID `followerId` started following the user with ID `followeeId`.
- `void unfollow(int followerId, int followeeId)` The user with ID `followerId` started unfollowing the user with ID `followeeId`.


### Example 1:
```
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
```


### Solution
We can use a hashmap to keep track of which user is following who by mapping `userId` to set of `userIds` representing the people they are following. Now for storing the tweets we can have a single list for all user tweets. So whenever `postTweet()`, we just add it to this list. Note that this also means that tweets closer to end of the list are more recent, and the end being our most recent. 

So for the `postTweet()` we just need to add the tweet to the list: `(userId, tweetId)`. Then for `follow` and `unfollow` we just need to add or remove the `followeeId` from the `followerId`'s set of ids since `followerId` follows `followeeId`. For the `getNewsFeed()` we will utilize the fact that most recent posts are at the end. So we need to do is iterate backwards until we either added 10 tweets or our list is empty. When deciding when to add the tweet, we must check the user id of tweet. Since the user's feed should only show their own tweets along with the people they are following: make sure the user id of the tweet equals the `userId` or it is the id of on the people they are following.

