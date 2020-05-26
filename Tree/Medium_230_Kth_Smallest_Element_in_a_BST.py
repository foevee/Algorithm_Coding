"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.


Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:
The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.


Solutions: Three ways
1) DFS In-order traversal (recursive, this way is optimal)
We are using Depth-First-Search to do in-order traversal. Use a count to track our process, init to k, meaning k distance away from target
Recursively searching from the bottom left tree, to its root, and its right tree. Continue going up in the same way
Each time, when finishing visiting a node's left tree, count -= 1, since we only get smaller element when visiting left tree of curr node
(in fact, this will work for the seemingly right nodes/root nodes, since when they have no further left node (or have been finished), visiting return (None) and then conunt -1 when coming back to those right/root nodes)
In this way, we are actually visiting from the smallest value to the kth smallest value (count -1 one by one)
When count==0, the current root.val is our target (the kth smallest element in a BST)

We use recursive functions and a global variable count to do the BST with the operations above.


Complexity: Time O(N)

2) DFS In-order traversal (iterative)
Similar as 1), but just using a stack to do iterative looping rather than recursion
Complexity: Time O(N) best

3) Binary Search on Tree (not optimal for this problem)
Use an extra count pointer to do binary search, 
  use a helper function to count the left tree nodes number, save as count
  if count==k-1, means the current root.val is just the kth smallest elem, return root.val
  if count>=k, search on its left tree, target is still k (notice k is from the bottom-left to above, still need to find the k smallest)
  if count<k-1, search on its left tree, target changed to k-count-1 (since left_tree + root has count+1, right tree only needs to search the k-count-1 smallest elem, which is indeed the global kth smallest elem)
Complexity: Time: O(N) best, O(N^2) worst

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## Method 1: DFS in-order traversal (recursive)
## Time Complexity: O(N)
class Solution:
    #use a class variable to save the kth smallest value and the count of distance towards the kth value
    val = 0 
    count = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = k
        self.DFS_traversal(root)
        return self.val
    
    def DFS_traversal(self, root):
        #we always use in-order traversal, from left-tree to root to right tree
        #in this process, the count will -1 once finishing visiting left tree
        #there must have be a unique point for count = 0, where the kth value exists
        if not root:
            return
        self.DFS_traversal(root.left)
        self.count -= 1  #only decrease one when done visiting the left tree node
        if self.count==0:
            self.val = root.val
            return
        self.DFS_traversal(root.right)
        return


## Method 2: DFS in-order traversal (recursive)
## Time Complexity: O(N) best
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        stack = []
        count = k
        stack.append(root)
        stack.append(root.left)
        while(stack):
            if(stack[-1]): #once not reaching the end of left node, keep pushing in stack
                stack.append(stack[-1].left)
                continue
            left_ = stack.pop() #this is none
            root_ = stack.pop() #get its root
            count -= 1
            if (count==0):
                return root_.val
            stack.append(root_.right)  #in-order traversal, left-root-right
        return -1


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #count the left tree nodes
        if not root:
            return 0
        count = self.count_tree(root.left)
        if (count==k-1):
            return root.val
        elif (count>=k): #still search its left tree, target k unchanged (still need to find the kth smallest from the bottom-left)
            return self.kthSmallest(root.left, k)
        else:  #search it right tree, new target k-count-1 (what left in right tree is to find the k-count-1th smallest)
            return self.kthSmallest(root.right, k-count-1) #since left + root = count + 1
        
    def count_tree(self, root):
        if not root:
            return 0
        return 1+self.count_tree(root.left)+self.count_tree(root.right)