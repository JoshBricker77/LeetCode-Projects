class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map opening brackets to their respective closing brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        # Stack to keep track of open brackets
        stack = []

        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if the popped element matches the expected opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty at the end, all brackets were properly closed
        return not stack
