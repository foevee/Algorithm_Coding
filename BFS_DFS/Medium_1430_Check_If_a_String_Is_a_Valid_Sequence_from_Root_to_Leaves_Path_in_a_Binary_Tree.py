"""
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

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
Use DFS to search the valid path with a track of the pos in the array
  At each node, general logic is to check at each DFS step
    1) if root node is equal to the array[pos] element 
    2) if DFS on left child or right child is true
    both 1) and 2) need to satisfy to return true
  Ending position at each DFS step:
    (success) if root.val = arr[pos] and root.left = root.right = None and pos = len(arr)-1, we find the valid path, return true
    (failure) if the root is None (not valid path since we want leaf node as end), return false
    (failure) if the pos>=len(arr), we do not end in pos=len(arr)-1 successfully but just keep DFS (means failure), so return false

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.DFS(root, arr, 0)
    
    def DFS(self, root, arr, pos):
        #ending condition: root should only end in a leaf and pos should end in len(arr)-1
        if root==None or pos>=len(arr): 
            return False #if pos reaching the end return true otherwise false
        
        root_equal = root.val==arr[pos] #if we do not have pos>=len(arr) above, we might get indexing error here
        #make sure the valid path end in the leaf node (root has no child anymore)
        if root_equal and pos==len(arr)-1 and root.left==None and root.right==None:
            return True
        
        left = self.DFS(root.left, arr, pos+1)
        right = self.DFS(root.right, arr, pos+1)

        return root_equal and (left or right)