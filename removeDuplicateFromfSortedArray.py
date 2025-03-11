from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place such that each unique element appears only once.
        The relative order of elements is preserved.

        Args:
        nums (List[int]): A sorted list of integers.

        Returns:
        int: The number of unique elements.
        """
        # Edge case: If the array is empty, return 0
        if not nums:
            return 0

        # Initialize the slow pointer at index 0 (first unique element)
        i = 0

        # Iterate through the array with the fast pointer (j)
        for j in range(1, len(nums)):
            # If we find a new unique element
            if nums[j] != nums[i]:
                i += 1  # Move slow pointer forward
                nums[i] = nums[j]  # Update the position with new unique element

        # The length of the unique elements in the array is (i + 1)
        return i + 1

# Example usage:
nums = [1, 1, 2]
sol = Solution()
k = sol.removeDuplicates(nums)
print(f"Number of unique elements: {k}")
print(f"Modified nums array: {nums[:k]}")  # Output should be [1, 2]
