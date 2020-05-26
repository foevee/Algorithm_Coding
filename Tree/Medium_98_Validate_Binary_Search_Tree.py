"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Method 1: Using Depth First Search
Keeping the lower and upper limit set for validating each node 
(not only comparing with its direct parent, but also with its previous parent)
"""

def dfs(node, lower, upper):
     #To valid if the tree is a Binary Search Tree (BST)
    #We need to remember the upper or lower limit for each child node, so the child node will not only compare with its parent but also the previous parent root.
    if(not node):
        return True
    if(node.val>=upper or node.val<=lower):
        return False
    return (dfs(node.left,lower,node.val) and dfs(node.right,node.val,upper))
        
        
        
def isValidBST(root):
    #since we need upper and lower parameters, we set another dfs function
    return dfs(root,float("-inf"),float("inf"))


"""
Method 2, iteration method

Note, any recursion can be substituted with iteration (use a queue)
"""
#    def isValidBST(self, root):
#    if not root:
#        return True
#            
#    stack = [(root, float('-inf'), float('inf')), ] 
#    while stack:
#        root, lower, upper = stack.pop()
#        if not root:
#            continue
#        val = root.val
#        if val <= lower or val >= upper:
#            return False
#        stack.append((root.right, val, upper))
#        stack.append((root.left, lower, val))
#    return True  




"""
Method 3: <!!! New> Inorder traversal
visit the tree in the left->root->right order, to make a ascending list
if the list acquired is not ascending, then we say the tree is an invalid bst
"""
def dfs_traversal(root):
    num=[]
    if(not root):
        return num
    num.extend(dfs_traversal(root.left))
    num.append(root.val)
    num.extend(dfs_traversal(root.right))
    return num
def isValidBST(root):
    if(not root):
        return True
    num=dfs_traversal(root)
    prev=num[0]
    for i in range(1,len(num)):
        if(num[i]!=None and num[i]<=prev):
            return False
        prev=num[i]
    return True
