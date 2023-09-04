"""Leetcode: Merge Sorted Array"""
from typing import List

testcase_1 = [1, 2, 3, 0, 0, 0]
testcase_2 = [2, 5, 6]

class Solution:
    def merge(self, nums1: List[int], nums2: List[int], nums2_len: int):
        """Merge sorted"""
        for idx in range(1, nums2_len+1):
            nums1[-idx] = nums2.pop()
        nums1.sort()

if __name__ == "__main__":
    inout = list(testcase_1)
    Solution().merge(inout, testcase_2, len(testcase_2))
    assert inout == [1, 2, 2, 3, 5, 6]
    print("testcase 1 PASSED")
