from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = defaultdict(int)
        substring = defaultdict(int)
        for char in s1:
            perm[char] += 1

        start = 0

        for end in range(len(s2)):
            if substring == perm:
                return True

            substring[s2[end]] += 1

            while start < end and (s2[start] not in perm or substring[s2[start]] > perm[s2[start]]): 

                substring[s2[start]] -= 1

                if substring[s2[start]] <= 0:
                    del substring[s2[start]]

                start += 1

        return substring == perm