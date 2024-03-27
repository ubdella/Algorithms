# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        dummy = head
        while(dummy != None):
            if dummy in seen:
                return True
            seen.add(dummy)
            if dummy!= None:
                dummy = dummy.next
        return False
        