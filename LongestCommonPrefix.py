#leetcode 14: Longest Common Prefix
#Write a function to find the longest common prefix string amongst an array of strings.
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: if the list is empty, return an empty string
        if not strs:
            return ""

        # Sort the list of strings. This helps in easily finding the common prefix
        strs.sort()

        # Take the first and last strings after sorting
        first, last = strs[0], strs[-1]

        # Initialize an index to track the common prefix length
        i = 0

        # Compare characters of the first and last string until a mismatch is found
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        # The common prefix is the substring of the first string up to index i
        return first[:i]
