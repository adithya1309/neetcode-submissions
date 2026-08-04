# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maximum_depth = 0
        if root is None:
            return 0
        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)
        maximum_depth = 1 + max(right_depth, left_depth)

        return maximum_depth
