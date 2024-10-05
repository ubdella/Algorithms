# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head: ListNode, root: TreeNode) -> bool:
            # If we've reached the end of the linked list, we've found a match
            if not head:
                return True
            
            # If we've reached the end of the tree path but not the end of the list, no match
            if not root:
                return False
            
            # If the current values match, continue checking
            if root.val == head.val:
                return dfs(head.next, root.left) or dfs(head.next, root.right)
            
            # If values don't match, return False
            return False

        # Base case: if the tree is empty, return False
        if not root:
            return False

        # Check if the linked list starts from the current node
        if dfs(head, root):
            return True

        # If not, recursively check left and right subtrees
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)