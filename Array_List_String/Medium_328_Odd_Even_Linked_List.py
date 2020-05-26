"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...



Solution: Two pointers
Use two pointers to loop: 
  One (odd) to loop through odd index term and link them together, another (even) to loop through even terms and link them
  In extra, use a even_head to save the first item of even sub-linked list
  Finally, link the end of the odd sub-linked list (using end pointer - odd) to the head pointer (even_head) of the even sub-linked list
  Done!
  
Complexity: Time O(N), Space: O(1)

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd, even, even_head = head, head.next, head.next
        while(odd.next and even.next):  #notice both need to be not null (one is ahead of another), we use both below
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
            
        #concatenate two sub-linkedlists
        odd.next=even_head
        return head