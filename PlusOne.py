from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments the large integer represented as an array by one.

        Args:
        digits (List[int]): A list of digits representing an integer.

        Returns:
        List[int]: A list of digits representing the incremented integer.
        """
        # Start from the last digit (least significant)
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is not 9, we can simply increment it
            if digits[i] < 9:
                digits[i] += 1  # Add 1 to the current digit
                return digits   # Return the updated list since we are done

            # If the digit is 9, set it to 0 and continue the loop
            digits[i] = 0

        # If we exit the loop, it means all digits were 9 (e.g., [9,9,9] -> [1,0,0,0])
        return [1] + digits

# Example usage:
sol = Solution()
print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(sol.plusOne([9]))  # Output: [1,0]
print(sol.plusOne([9,9,9]))  # Output: [1,0,0,0]
