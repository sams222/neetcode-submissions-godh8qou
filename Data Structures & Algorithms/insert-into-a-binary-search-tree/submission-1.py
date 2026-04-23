# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def isLeaf(node):
            if node.left or node.right:
                return False
            else:
                return True

        newNode = TreeNode(val)

        if root is None:
            return newNode

        curr = root

        while not isLeaf(curr):

            if curr.left and val < curr.val:
                curr = curr.left
            elif curr.right and  val > curr.val:
                curr = curr.right

            else:
                if val < curr.val:
                    curr.left = newNode
                else:
                    curr.right = newNode
                return root

        if val < curr.val:
            curr.left = newNode
        else:
            curr.right = newNode

        return root 

            



        
        