"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
       1
      / \
     2   3
    /  
   4
Output: false

Example 2:
Input: [1,2,3,null,null,4,5], x=4, y=5
    1
   / \
  2   3
     /  \
    4    5
Output: false

Example 2:
Input: [1,2,3,4,null,null,5], x=4, y=5
    1
   / \
  2   3
 /     \
4       5
Output: true

Method 1: BFS
Use a Breadth First Search to search each depth node, using a queue (list) to push in child node and pop out father node
  during  the search at each depth, compare with x and y, update the x_depth and y_depth, and then determine true or false
Complexity: Time O(V+E), Space O(V)

Method 2: DFS
Use a Depth First Search to search the depth of x, y, return its depth and father, compare to determine true or false
Complexity: Time O(V+E), Space O(1)

!!!Notice: The two search all require an important prerequisite: each value only appear in the node uniquely! 
  (No replicates, otherwise, we can not find the exact value and comapre)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## Method 1: BFS
def isCousins(root: TreeNode, x: int, y: int) -> bool:
  if (not root) or root.val==x or root.val==y:
    return False      
    x_depth, y_depth = 0, 0
        
    queue = []
    queue.append((0,root))  #depth idx and TreeNode
    while (queue):
      idx, father = queue.pop(0)
      if not father:  #father=None
        continue
      before_no_update = (x_depth==0 and y_depth==0) #both not updated before
            
        #uniquely updated
      if father.left:
        x_depth = idx+1 if father.left.val == x else x_depth
        y_depth = idx+1 if father.left.val == y else y_depth
        queue.append((idx+1, father.left))
      if father.right:
        x_depth = idx+1 if father.right.val == x else x_depth
        y_depth = idx+1 if father.right.val == y else y_depth
        queue.append((idx+1, father.right))
            
        #both not 0, already updated (unique)                             
      if x_depth and y_depth:
        if before_no_update and x_depth==y_depth: #same father
          return False
        else:
          return x_depth==y_depth #not the same father
        
      return False #not found


## Method 2: DFS (faster)
def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
  if (not root) or root.val==x or root.val==y:
    return False
        
  #root, depth, father, find_val
  _, x_depth, x_father = self.DFS(root, 0, -1, x)
  _, y_depth, y_father = self.DFS(root, 0, -1, y)
        
  return True if x_depth==y_depth and x_father!=y_father else False

## helper function    
def DFS(self, root, depth, father, x):
  if not root:
    return (False, depth, father)
  if root.val==x:
    return (True, depth, father)

  is_l, l_dep, l_father = self.DFS(root.left, depth+1, root.val, x)
  is_r, r_dep, r_father = self.DFS(root.right, depth+1, root.val, x)
        
  return (is_l, l_dep, l_father) if is_l else (is_r, r_dep, r_father)


            