class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Computes the square root of x using binary search.

        Args:
        x (int): A non-negative integer.

        Returns:
        int: The square root of x, rounded down.
        """

        # Edge case: Square root of 0 and 1 is itself
        if x == 0 or x == 1:
            return x

        # Binary search range (we never need to check beyond x//2)
        low, high = 1, x // 2
        result = 1  # Stores the best possible square root

        while low <= high:
            mid = (low + high) // 2  # Find middle value
            squared = mid * mid  # Compute mid^2

            if squared == x:
                return mid  # Exact square root found
            elif squared < x:
                result = mid  # Store possible answer
                low = mid + 1  # Search in the right half
            else:
                high = mid - 1  # Search in the left half

        return result  # Return the stored best result

# Example usage:
sol = Solution()
print(sol.mySqrt(4))   # Output: 2
print(sol.mySqrt(8))   # Output: 2
print(sol.mySqrt(25))  # Output: 5
print(sol.mySqrt(1))   # Output: 1
print(sol.mySqrt(0))   # Output: 0
print(sol.mySqrt(2147395599))  # Large test case
