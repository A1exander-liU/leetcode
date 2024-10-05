# Problem

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words
`beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

### Example 1

```bash
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
```

### Example 2

```bash
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

### Solution

Given that we want to find shortest sequence we should use BFS. DFS would require to try every single path and determine the min path from
them all which means it always has to traverse the whole graph.

Because for each word in sequence only differs by 1 letter, each word's neighbors would be all the words that are only differ by 1 from it.
To determine difference we can iterate over the indices and compare the character at each index and count how many characters differ, since
the words are all the same length it would not matter which string is chosen to be iterated over.

To track the length of that is shortest, we will store the length along with the word in the queue: `(word, length)` so when storing initial:
`(beginWord, 1)` since `beginWord` is considered as part of the sequence as well. Then every time we move to its neighbor and add to queue,
its length would be `length + 1` as we moved one level from our current word. Once we our current word is same as `endWord` we can just return the length

Optimization:
We iterate over the character of each word instead and changing from `a - z` and checking if this new word is in `wordList`. If its in `wordList` we add to queue and visited to make sure we don't find same word again.

- If we have `hit` in example 1 we would do:
  - For first letter: `ait, bit, cit, ... zit` we find nothing
  - For second letter: `hat, hbt, hct, ..., hzt` we find "hot"
- For third letter: `hia, hib, hic, ... hiz` we find nothing

Doing this spends less operations on worst case if you consider the input constraints as max word length is `10` and max length of `wordList`is `5000`.

For determining neighbors of a word using distance:

- Have to check each word and also each character of word
  `Each word needs to check 10 letters for all words so: 5000 words * 10 = 50000 operations`

For checking letter by letter:

- Have to iterate over each letter in word, checking whole alphabet and constructing new string
  `Each word needs to be iterated over, each letter needs to be iterated over entire alphabet: 10 for word length * 26 for alphabet = 260`
