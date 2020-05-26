"""
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]
       1
      / \
     2   3
Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
Output: 42

Method:
Use a Depth First Search to find the maximum single path of each node
  add the "left path sum + root value + right path sum" to get the max sum of each node
  notice we do not need to make all summation of all "left+right" path of a node, if any single path sum < 0, we can drop that and count as 0
  we use DFS to return the maximum single path value (not both), which is root.val+max(left, right)
  we use an extra max_sum to save the maximum path sum during the DFS search

Complexity: Time O(V+E), Space O(1)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_sum = float("-inf")
    def maxPathSum(self, root: TreeNode) -> int:
        self.DFS(root) #will update max_sum
        return self.max_sum
        
    def DFS(self, root):  #returning the max single child path (not both) sum of a node
        if not root:
            return 0
        val = root.val
        #does not need to include all nodes, if path sum < 0, then not count (take left==0)
        left = max(self.DFS(root.left), 0) #single path of left
        right = max(self.DFS(root.right), 0) #single path of right
        self.max_sum = max(self.max_sum, left+val+right)
        return val + max(left, right)  #returning the max single child path(not both)
