"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 19


Solution:
The problem is to calculate the number of unique BST. To do so, we need to define two functions:
G(n): the number of unique BST for a sequence of length n.
F(i, n), 1 <= i <= n: the number of unique BST, where the number i is the root of BST, and the sequence ranges from 1 to n.

1. Given the above definitions, we can see that the total number of unique BST G(n), is the sum of BST F(i) using each number i as a root.
i.e. G(n) = F(1, n) + F(2, n) + ... + F(n, n). 
Particularly, the bottom cases, there is only one combination to construct a BST out of a sequence of length 1 (only a root) or 0 (empty tree).
i.e. G(0)=1, G(1)=1. 

2. Given a sequence 1...n, we pick a number i out of the sequence as the root, then the number of unique BST with the specified root F(i), is the cartesian product of the number of BST for its left and right subtrees. 
i.e. F(i, n) = G(i-1) * G(n-i)	1 <= i <= n 
Combining the above two formulas, we obtain the recursive formula for G(n). i.e.

G(n) = G(0) * G(n-1) + G(1) * G(n-2) +... + G(n-1) * G(0) 
In terms of calculation, we need to start with the lower number, since the value of G(n) depends on the values of G(0) … G(n-1).

"""


#Method 1: Recursion with memorization
#Time O(n^2) ==> two loop layer, Space O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        counted = [-1]*(n+1)
        counted[0] = counted[1] = 1
        if n>=2: counted[2] = 2
        self.countTrees(n, counted)
        return counted[n]
    
    def countTrees(self, n, counted):
        if counted[n]!=-1: return counted[n]
        
        mid = n//2 if n%2==0 else n//2+1
        total = 0
        
        #for i in root, left tree has i-1 child (count its num), right tree has n-i child (count its num)
        #count combinations (use *) of left and right substree number

        for i in range(1, mid+1): #we count by *2 so only use first half
            num = self.countTrees(i-1, counted)*self.countTrees(n-i, counted)
            #for i and n-i, they are symmetric regarding left/right substree number, combs (*) should be same
            if i<=n-i: num*=2 #omit only when n is odd and i reach mid, which is i<=n-i (i=n-i+1)
            total += num
        
        counted[n] = total
        
        return total

#Method 2: Dynamic Programming
#Rewrite the above recursion logic into recursion, in order from i=1 to i=n, each time count j=1 to mid=i//2 (or i//2+1)
#Time O(n^2), Space O(n) ===> i.e. G(n) = 1 (n=1) + 2/2 (n=2, from 1 to mid) + 3/2 (n=3, mid=3/2) + ... + n/2 = (1+n)*n/4 ~ O(n^2)
class Solution:
    def numTrees(self, n: int) -> int:
        if n<=1: return 1
        counted = [0]*(n+1)
        counted[0] = counted[1] = 1
        
        for i in range(2,n+1):
            mid = i//2 if i%2==0 else i//2+1
            for j in range(1, mid+1):
                num = counted[j-1]*counted[i-j]
                if j<=i-j: num *= 2 #omit only when n is odd and i reach mid, which is i<=n-i (i=n-i+1)
                counted[i] += num
        
        return counted[n]
    
    