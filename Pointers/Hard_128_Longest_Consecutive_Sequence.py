'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
### Method 1: Sort
### Complexity: O(nlogn) time, O(1) space
### sort first, then count the length of each consecutive sequence
def longestConsecutive(self, nums: List[int]) -> int:
    nums = sorted(list(set(nums)))
    if len(nums)<=1: return len(nums)
    prev = ''
    length = 0
    maxlen = 1
    for num in nums:
        if prev!='' and num==prev+1: 
            length += 1
            prev = num
            maxlen = max(maxlen, length)
        else:
            length = 1
            prev = num
            
            
    return maxlen

### Method 2: Optimal: Hashset (start counting from each start of consecutive sequence)
### Complexity: O(n) time, O(1) space
### use hashset to get unique numbers, then loop through each number in O(n) time
### if this number is the start (num-1 not in list), then keep sub-looping to count its consecutive sequence and update the length
### notice once this sequence group has been visited in inner-loop, other numbers in this sequence will not be started / re-visited from the outer-loop (since they are not the start)
def longestConsecutive(self, nums: List[int]) -> int:
    numset = set(nums)
        
    if len(nums)<=1: return len(nums)
    
    maxlen = 1
    for start in numset:
        if start-1 not in numset:  #means this number could be a start of a consecutive sequence
            num = start+1
            while num in numset:
                num += 1
            maxlen = max(maxlen, num-start)    
            
    return maxlen   
            

### Method 3
### Notice we can also use union-find to solve this problem.
### (Could investigate for this later)
