class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        substring = set()

        for end in range(len(s)):
            prev_length = len(substring)
            substring.add(s[end])
            new_length = len(substring)

            max_length = max(max_length, new_length) 

            # if we add to set and len didn't change that means s[end] already exists (it's a dupe)
            if new_length == prev_length:
                # keep removing until duplicate element, removing the dupe as well
                while start < end:
                    substring.remove(s[start])

                    if s[start] == s[end]:
                        start += 1
                        break

                    start += 1
                
                # make sure to add s[end] to the set (since we removed the dupe element as well)
                substring.add(s[end])

        return max_length