from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays nums1 and nums2 into nums1 in-place.

        Args:
        nums1 (List[int]): First list with length m + n.
        m (int): Number of initialized elements in nums1.
        nums2 (List[int]): Second sorted list with n elements.
        n (int): Number of initialized elements in nums2.

        Returns:
        None: Modifies nums1 in-place.
        """
        # Pointers to the last initialized elements
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1  # Last position in nums1

        # Merge from the back
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 still has elements left
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
