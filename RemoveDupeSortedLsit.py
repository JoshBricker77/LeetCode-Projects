from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Removes duplicates from a sorted linked list.

        Args:
        head (ListNode): The head of a sorted singly-linked list.

        Returns:
        ListNode: The head of the modified list with duplicates removed.
        """
        current = head  # Start with the head of the list

        # Traverse the list
        while current and current.next:
            if current.val == current.next.val:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next distinct element
                current = current.next

        return head  # Return the updated list
