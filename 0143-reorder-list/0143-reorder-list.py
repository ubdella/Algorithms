# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        array = []
        tail = head
        while tail:
            array.append(tail)
            tail = tail.next
        
        l, r = 0, len(array) - 1
        
        while l < r and array[l].next != array[r]:
            array[l].next = array[r]
            array[r].next = array[l + 1]
            r -= 1
            l += 1
        array[r].next = None
        return head
            