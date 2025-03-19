class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns the result as a binary string.

        Args:
        a (str): First binary string.
        b (str): Second binary string.

        Returns:
        str: Sum of the two binary numbers in binary format.
        """
        # Convert both binary strings to integers, add them, then convert back to binary
        return bin(int(a, 2) + int(b, 2))[2:]

# Example usage:
sol = Solution()
print(sol.addBinary("11", "1"))      # Output: "100"
print(sol.addBinary("1010", "1011")) # Output: "10101"
