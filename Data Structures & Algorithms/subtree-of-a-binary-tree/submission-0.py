# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node, subRoot):
            stack = [(node, subRoot)]

            while stack:
                noder, nodesr = stack.pop()
            
                if not noder and not nodesr:
                    continue
                if not noder or not nodesr or noder.val != nodesr.val:
                    return False
                stack.append((noder.right, nodesr.right))
                stack.append((noder.left, nodesr.left))

            return True

        if not root:
            return False
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
