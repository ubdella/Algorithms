# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = hare = head
        while tortoise:
            if not hare.next:
                return tortoise
            if not hare.next.next:
                return tortoise.next
            tortoise = tortoise.next
            hare = hare.next.next
            
        
            