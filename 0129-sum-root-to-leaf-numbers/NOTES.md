```py
class Solution:
def sumNumbers(self, root: TreeNode) -> int:
if not root:
return 0
def dfs(node, num):
if not node.left and not node.right:
return num * 10 + node.val
left_sum = dfs(node.left, num * 10 + node.val) if node.left else 0
right_sum = dfs(node.right, num * 10 + node.val) if node.right else 0
return left_sum + right_sum
return dfs(root, 0)
```
​
We start by checking if the root exists or not. If the root is `None`, then there are no root-to-leaf paths and we return `0`.
We define a helper function dfs that takes two arguments:
`node`: The current node that we are visiting
`num`: The value of the path so far, i.e., the value obtained by concatenating the values of all the nodes from the root to the current node.
Inside the dfs function, we first check if the current node is a leaf node or not. If it is a leaf node, we return the sum of the path so far and the value of the current node.
If the current node is not a leaf node, we recursively call the dfs function on its left and right children (if they exist) and add their return values to get the sum of all the root-to-leaf paths in the binary tree.
Finally, we return the total sum of all the root-to-leaf paths.
​
In this solution, we are using Depth-First Search (DFS) algorithm to traverse the binary tree in a recursive manner.
We are passing the value of the path so far (`num`) as an argument to the dfs function, and updating it by multiplying it with 10 and adding the value of the current node.
​
This way, we are concatenating the values of all the nodes from the root to the current node, and getting the total path sum when we reach a leaf node.
​
This way, we are concatenating the values of all the nodes from the root to the current node, and getting the total path sum when we reach a leaf node.
The time complexity of this solution is O(n), where n is the number of nodes in the binary tree, as we are visiting each node once. The space complexity is also O(n), as the maximum size of the call stack is equal to the height of the binary tree.