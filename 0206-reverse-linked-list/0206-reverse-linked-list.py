class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i, j = None, head
        while j:
            temp = j.next
            j.next = i
            i = j
            j = temp
        return i