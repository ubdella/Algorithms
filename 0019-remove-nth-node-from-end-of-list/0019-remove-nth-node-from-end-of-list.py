# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Use two pointers: 'slow' and 'fast'
        slow = fast = head

        # Move the 'fast' pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # If 'fast' is None, it means we need to remove the head node
        if not fast:
            return head.next

        # Move both 'slow' and 'fast' until 'fast' reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return head
            