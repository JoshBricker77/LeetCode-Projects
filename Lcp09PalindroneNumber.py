class Solution:
    def isPalindrome(self, x):
        """
        Check if an integer is a palindrome. An integer is a palindrome
        when it reads the same backward as forward.

        :param x: Integer, the number to check.
        :return: Boolean, True if x is a palindrome; otherwise, False.
        """
        # Convert the integer to a string
        original_str = str(x)

        # Reverse the string using slicing
        reversed_str = original_str[::-1]

        # Compare the original string with the reversed string
        return original_str == reversed_str

# Create an instance of the Solution class
sol = Solution()
