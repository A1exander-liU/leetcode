from typing import List
from collections import deque
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        letters = string.ascii_lowercase
        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while len(q) > 0:
            word, length = q.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for letter in letters:
                    candidate = f"{word[:i]}{letter}{word[i + 1 :]}"
                    if candidate in visited:
                        continue
                    if candidate in wordSet:
                        q.append((candidate, length + 1))
                        visited.add(candidate)

        return 0
