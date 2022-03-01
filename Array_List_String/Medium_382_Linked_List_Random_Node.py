"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:
  Solution(ListNode head) Initializes the object with the integer array nums.
  int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.
 

Example 1:
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
 

Constraints:
The number of nodes in the linked list will be in the range [1, 104].
-104 <= Node.val <= 104
At most 104 calls will be made to getRandom.
 

Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?



#Reservoir Sampling
#https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling
#Problem:
#   Choose k entries from n numbers. Make sure each number is selected with the probability of k/n
#Basic idea:
#   Choose 1, 2, 3, ..., k first and put them into the reservoir.
#   For k+1, pick it with a probability of k/(k+1), and randomly replace a number in the reservoir.
#   For k+i, pick it with a probability of k/(k+i), and randomly replace a number in the reservoir.
#   Repeat until k+i reaches n
  
Complexity: Time O(N), Space: O(1)

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def __init__(self, head: Optional[ListNode]):
        self.head = head
    
    def getRandom(self) -> int:
        res = self.head.val
        p = self.head.next
        #choose k reservoir step by step, here k=1, start i = 1 to increase
        k, i = 1, 1
        while p:
            #1. One way: randint()
            #num = random.randint(1,i+1) #inclusive, choose within [1,i+1]
            #if num <= k: res = p.val #here since k=1, means num=k=1, replace the reservoir number
            
            #2. Another way: random()
            prob = random.random() #fits in [0,1)
            if prob <= k/(k+i): res = p.val #replace the reservoir with k/(k+i) prob
            i += 1
            p = p.next
        
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()