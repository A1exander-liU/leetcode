from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []

        i1 = 0
        i1_len = len(nums1)
        i2 = 0
        i2_len = len(nums2)
        total = i1_len + i2_len

        while i1 < i1_len and i2 < i2_len:
            if nums1[i1] <= nums2[i2]:
                result.append(nums1[i1])
                i1 += 1
            else:
                result.append(nums2[i2])
                i2 += 1

        while i1 < i1_len:
            result.append(nums1[i1])
            i1 += 1

        while i2 < i2_len:
            result.append(nums2[i2])
            i2 += 1

        if total % 2 == 1:
            return result[total // 2]
        else:
            return (result[total // 2] + result[total // 2 - 1]) / 2
