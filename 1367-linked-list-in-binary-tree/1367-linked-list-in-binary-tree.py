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

    def dfsHelper(self, root, head):
        if head == None:return True
        if root == None:return False
        if root.val != head.val:return False
        return self.dfsHelper(root.left, head.next) or self.dfsHelper(root.right, head.next) 

    def dfs(self, root, head):
        if root == None:
            return False
        if root.val == head.val:
            if self.dfsHelper(root.left, head.next):
                return True
            if self.dfsHelper(root.right, head.next):
                return True
        if self.dfs(root.left, head):
            return True
        if self.dfs(root.right, head):
            return True
        return False
    def isSubPath(self, head, root):
        return self.dfs(root, head)