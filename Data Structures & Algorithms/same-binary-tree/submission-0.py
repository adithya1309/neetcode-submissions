# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        parray = []
        qarray = []
        
        stackp = [p]
        while stackp:
            node = stackp.pop()
            if not node:
                parray.append(None)
                continue
            parray.append(node.val)
            stackp.append(node.right)
            stackp.append(node.left)
        stackq = [q]
        while stackq:
            node = stackq.pop()
            if not node:
                qarray.append(None)
                continue
            qarray.append(node.val)
            stackq.append(node.right)
            stackq.append(node.left)

        return parray == qarray