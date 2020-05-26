"""
Given an array nums of n integers where n > 1,  return an array output 
    such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]  Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


Method:
Use loops for 2 times, roll over the whole array two times
    first forward to get all cum mutiplication before each element itself,
    then backward to further mutiply by all number after each elemnt itself
Complexity: O(N) Time, O(1) extra space 
"""

def productExceptSelf(self, nums: List[int]) -> List[int]:
    multi = 1 #use to track cum mutiply
    prod = []
    ##first forward mutiply, each element mutiply by all elements before it
    for num in nums:
        prod.append(multi)
        multi *= num
        
    multi = 1
    ##then backward mutiply, each element further mutiply by all elements after it
    for i in range(len(nums)-1,-1,-1):
        prod[i] *= multi
        multi *= nums[i]
    return prod