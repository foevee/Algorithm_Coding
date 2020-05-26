"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.


Method: Use a stack to loop through the nums2 list and save all num's next greater element
  whenever meeting the new number larger than previous stack element and stack is non-empty
  continue popping the stack numbers out and save this number and current number into the hashmap 
    (as {stack poped number : current number})
    means the current number is the stack poped number's next greater element
  when the above loop (poping) ends (condition no longer satisfied), we will push this new number into the stack

Then use this hashmap to find the next greater element of each nums1's number

*!*This is the classical stack method:
loop through the array and pop out whenver certain condition holds. After the popping loop ends, push back the new element into the stack
"""

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    #construct a stack to loop through nums2 and save each item's next greater elem
    stack = []
        
    next_greater = {} #use a dict to save next greater element
    for num in nums2:
        #find all its previous lesser element (thus num is their next greater elem)
        while(stack and num > stack[-1]):
            n = stack.pop()
            next_greater[n] = num
        #push new num in
        stack.append(num)
        
    #get element in dict, otherwise return -1
    result = [next_greater.get(num, -1) for num in nums1]
        
    return result
