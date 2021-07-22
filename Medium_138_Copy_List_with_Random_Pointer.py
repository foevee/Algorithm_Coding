"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#1. Direct way: O(N) space
# Iteratively visit the nodes and save old (copied) nodes
def copyRandomList(self, head: 'Node') -> 'Node':
    #return null if head is null
    if not head: return head
    visited = {}
    p = head
    pnew = Node(head.val)
    visited[p] = pnew

    while p:
        #copy random state node
        if p.random:
            if p.random not in visited:
                pnew.random = Node(p.random.val)
                visited[p.random] = pnew.random
            else:
                pnew.random = visited[p.random]
        
        #copy next state node
        if p.next:
            if p.next not in visited:
                visited[p.next] = Node(p.next.val)
            pnew.next = visited[p.next]
        
        #move p and pnew
        p = p.next
        pnew = pnew.next
    
    return visited[head] #which is the copied head


#2. Optimal way: O(1) space
def copyRandomList(self, head: 'Node') -> 'Node':
    #To avoid save previous initialized old node (in random setting), we can use the following algorithm
    #old: A --> B --> C --> D
    #interwaved: A --> A' --> B --> B' --> C --> C' --> D --> D'
    #Three steps:
    # - Iterate the original list and duplicate each node next to original one.
    # - Iterate the new list and assign the random pointer for each duplicated node.
    # - Restore the original list and extract the duplicated nodes.
    
    if not head: return head
    #1. first loop: insert a copy of node to the next pos of original node
    p = head
    while p:
        pnew = Node(p.val)
        pnew.next = p.next
        p.next = pnew
        p = pnew.next
    
    #2. second loop, link random state to new nodes following its previous original ones
    p = head
    while p:
        pnew = p.next
        if p.random is not None:
            pnew.random = p.random.next
        p = pnew.next
        
    #3. third loop, decompse new node out
    p, headnew = head, head.next
    while p:
        pnew = p.next
        p = pnew.next
        if p is not None:
            pnew.next = p.next
        
    return headnew