# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # If the root is None, there are no root-to-leaf paths
        # and the sum of all paths is 0.
        if not root:
            return 0
        
        # Helper function to perform DFS traversal of the binary tree
        def dfs(node, num):
            # If the current node is a leaf node, return the sum of
            # the path so far and the value of the current node.
            if not node.left and not node.right:
                return num * 10 + node.val
            
            # If the current node is not a leaf node, recursively call the
            # dfs function on its left and right children (if they exist)
            # and add their return values to get the sum of all the
            # root-to-leaf paths in the binary tree.
            left_sum = dfs(node.left, num * 10 + node.val) if node.left else 0
            right_sum = dfs(node.right, num * 10 + node.val) if node.right else 0
            return left_sum + right_sum
        
        # Call the dfs function on the root node, passing the initial path sum as 0.
        return dfs(root, 0)
