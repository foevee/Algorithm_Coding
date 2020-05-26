"""
Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 
1 <= preorder.length <= 100
The values of preorder are distinct.


Solution: 
Use a stack to do track the parent-child nodes (i.e. like Breadth First Search) when looping through the preorder list
    1) First item in preorder list is the root to be considered, we push this root (node) to the stack.
    2) For next item in preorder list, there are 2 cases to consider:
        If value is less than last item in stack, it is the left child of last item.
        If value is greater than last item in stack, pop it until we find its parent.
            The last popped item will be the parent and the item will be the right child of the parent.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    stack = [root]
    for item in preorder[1:]:
        if item < stack[-1].val: #thie item is left child
            stack[-1].left = TreeNode(item)
            stack.append(stack[-1].left)  #push in the left child

        elif item > stack[-1].val: #this item is right child
            while stack and item > stack[-1].val: #keep pop out the left child until find the parent of this item (this item is the right child of the last poped-out parent)
                last_parent = stack.pop()  #pop out the last left child till find the parent of this right child (stop)
            last_parent.right = TreeNode(item) 
            stack.append(last_parent.right)  #need to append this right child, since it might have further left/right child, which appears later in the list with the preorder traversal
     
    return root