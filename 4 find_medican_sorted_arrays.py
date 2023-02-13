from typing import List


class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
    """
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = sorted(nums1+nums2)
        total_len = len(new_nums)
        middle_index = (total_len - 1) // 2
        if total_len % 2 == 0:
            return sum(new_nums[middle_index:middle_index + 2]) / 2
        return new_nums[middle_index]
