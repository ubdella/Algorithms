class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev, nxt = None, head
        while nxt:
            tmp = nxt.next
            nxt.next = prev
            prev = nxt
            nxt = tmp
        return prev
            
            
        
        