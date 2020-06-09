"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2  Output: [0,1,1]

Example 2:
Input: 5 Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.


Solution: Dynamic Programming
For each number, its binary digits of 1 is the same as those of its half plus the last digit is determined by if it's odd (1) or even(0)
  Because when we shift all digits of a number n to a bit up (left shift), then this number is doubled (x2), and the last digit is 0 
  So n and 2n has the same digits of 1, and 2n+1 has one more digit of 1 in the last digit than n
We can thus use this method to copy the previous (num//2) num's digit and the odd/even property to determine current number's digits
By looping one pass, we can thus get the result of all 0~num, which indeed use the dynamic programming.

Complexity: Time O(N) Space O(N)
"""

def countBits(self, num: int) -> List[int]:
    if num==0:
        return [0]
    result = [0 for i in range(num+1)]
    for i in range(1,num+1):
        result[i] = result[i//2] + i%2  #use a previous half number's digit and odd/even property to determine current digits
    return result

