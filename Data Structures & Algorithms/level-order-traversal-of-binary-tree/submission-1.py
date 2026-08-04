# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res = []
        q = deque()
        q.append(root)
        while q:
            lenq = len(q)
            level = []
            for i in range(lenq):
                root = q.popleft()
                if root:
                    level.append(root.val)
                    q.append(root.left)
                    q.append(root.right)
            if level:
                res.append(level)

        return res