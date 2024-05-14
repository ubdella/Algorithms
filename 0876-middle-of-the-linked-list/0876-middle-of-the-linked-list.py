# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        
        dummy = head
        
        store = {}
        
        while dummy:
            length += 1
            store[length] = dummy
            dummy = dummy.next
        
        mid = length//2+1
            
        return store[mid]
            