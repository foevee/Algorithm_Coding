"""
[Classic one!!!!!]
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 
Note:
-30000 <= A[i] <= 30000
1 <= A.length <= 30000


Method:
https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
(a great visulization above)

This problem is based on "Easy_53_Maximum_Subarray" problem, which uses the Kadane's algorithm (simple indeed, see below)

Kadane's algorithm:
loop through the array, and determine the maximum array sum upon current step, (must include current step) 
and at last take the maximum value among the array which is the maximum subarray sum
O(n) time

But Kadane's algorithm is used for finding the maximum continuous array sum without circulation or wrap
So for this problem, we also need to process when the wrapped (circular) array has the maxisum
We divide the problem into two cases:
1) Case 1: get the maximum sum using standard kadane's algorithm 
2) Case 2: find the maximum sum that includes wrapped (circular) elements
   in this case, if the wrapped array is max sum, then the left middle unwrapped one must be least sum
   [use Kadane's algorithm to find the least sum of unwrapped continuous array --> by reversing sign, change each x to -x and use Kadane]
   if turn all A[i] to -A[i], then we can get the max sum M now, reverse back then -M is the least sum of array,
       which is exactly from the middle array with the least sum (i.e. max negative sum)
## corner case:
   notice the reverse max_wrap_sum only works if case (1) max_kadane >0 
   (otherwise all element is non-positive and wrapped would get wrong result (0))
Then we compare case 1 and 2, only if case 1 originally >0, we return max(case 1 sum, case 2 sum), 
     otherwise (case 1 sum <=0), we take case 1 sum 
     (since now means all elements are non-positive, which is the corner case, the case 2 method does not work)

Complexity: Time: O(N), Space: O(1)
"""


def kadane(self, A):
    if not A:
        return 0
    curr_sum, max_sum = 0, A[0]
    for i in range(len(A)):
        curr_sum = curr_sum + A[i] if curr_sum>=0 else A[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum
        
def maxSubarraySumCircular(self, A: List[int]) -> int:
        
    # Case 1: get the maximum sum using standard kadane's algorithm 
    max_kadane = self.kadane(A)
  
    # Case 2: find the maximum sum that includes corner elements (wrapped)
    # in this case, if the wrapped array is max sum, then the left middle unwrapped one must be least sum
    # if turn all A[i] to -A[i], then the max sum will be the middle unwrapped one
    # notice the reverse max_wrap_sum only works if case (1) max_kadane >0 
    # (otherwise all element is non-positive and wrapped would get wrong result (0))
    total_sum = sum(A)
    reverse_A = [-a for a in A] 
    reverse_max_kadane = (-1)*self.kadane(reverse_A) #reverse to -sign get max unwrapped sum and reverse back
    max_wrap_sum = total_sum-(reverse_max_kadane)
      
    print(max_kadane, max_wrap_sum, total_sum)
    # The maximum circular sum will be discussed by two scenarios
    # 1) case 1 max_kadane>0, so wrapped might be larger, choose the maximum of two case's sum
    # 2) case 1 max_kadane already <0, means all element<=0, then any wrapped one could not be larger
     
    return max(max_kadane, max_wrap_sum) if max_kadane>0 else max_kadane
        