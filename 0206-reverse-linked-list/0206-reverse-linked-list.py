class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        front = None
        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev