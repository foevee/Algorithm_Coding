"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
 

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

2. Solution
A. BFS: 
use stack to track each node and depth, connect each to next using their depth
Time: O(N); Space: O(N)

B. DFS
use recursion to keep connecting node to its next, 
left child node's next is right child node, and track right node's next by checking if its father's node has next
"""

#method 1: BFS
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        if not root: return None
        stack.append((root, 0)) #track node and its depth
        lastnode, lastdepth = None, -1
        while stack:
            node, depth = stack.pop(0)
            if lastnode and lastdepth!=depth: lastnode.next = None
            elif lastdepth==depth: lastnode.next = node
                
            lastnode = node
            lastdepth = depth
                
            if node.left and node.right:  #perfect binary tree, must have both or none
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
            
        return root


#method 2: DFS (trickier, must only use O(1) memory space, as follow-up required)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(root, None)
        return root
    
    def dfs(self, node_curr, node_next):
        if not node_curr: return
        node_curr.next = node_next
        left, right = node_curr.left, node_curr.right
        if left:
            self.dfs(left, right)
            #right node's next need condiontion check (from father's next)
            if node_next: self.dfs(right, node_next.left)
            else: self.dfs(right, None)
        