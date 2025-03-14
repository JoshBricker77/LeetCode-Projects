from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Finds the index of target in nums, or the index where it should be inserted.

        Uses binary search for O(log n) time complexity.

        Args:
        nums (List[int]): A sorted list of distinct integers.
        target (int): The value we need to find or insert.

        Returns:
        int: The index where target is found or should be inserted.
        """

        # Initialize two pointers for binary search
        low, high = 0, len(nums) - 1

        # Perform binary search
        while low <= high:
            mid = (low + high) // 2  # Find the middle index

            if nums[mid] == target:
                return mid  # Found target at index mid
            elif nums[mid] < target:
                low = mid + 1  # Search right half
            else:
                high = mid - 1  # Search left half

        # If target is not found, `low` is the correct insertion index
        return low

# Example usage:
sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))  # Output: 2
print(sol.searchInsert([1,3,5,6], 2))  # Output: 1
print(sol.searchInsert([1,3,5,6], 7))  # Output: 4
print(sol.searchInsert([1,3,5,6], 0))  # Output: 0
