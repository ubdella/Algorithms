# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        lenMinusN, end = dummy, head
        while n > 0:
            end = end.next
            n -= 1
        while end:
            lenMinusN = lenMinusN.next
            end = end.next
        
        lenMinusN.next = lenMinusN.next.next
        return dummy.next
            