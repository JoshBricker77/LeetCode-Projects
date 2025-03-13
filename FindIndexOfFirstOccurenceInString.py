class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Finds the first occurrence of `needle` in `haystack`.

        Args:
        haystack (str): The main string where we are searching.
        needle (str): The substring we need to find.

        Returns:
        int: The index of the first occurrence of `needle` in `haystack`,
             or -1 if `needle` is not found.
        """
        # Python has a built-in method called `find()` that finds the first occurrence of a substring.
        # It returns the index if found, or -1 if not found.
        return haystack.find(needle)

# Example usage:
sol = Solution()
print(sol.strStr("sadbutsad", "sad"))  # Output: 0, since "sad" first appears at index 0
print(sol.strStr("leetcode", "leeto"))  # Output: -1, since "leeto" is not in "leetcode"
