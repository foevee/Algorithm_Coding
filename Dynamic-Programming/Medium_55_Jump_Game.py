"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4] Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4] Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.


Solution:
Iterate through each index, update the max reaching value till that index. 
Notice that we are looping with dynamic range -- the index range could not exceed the max_reach value
   since we could not go to the index which we could not reach for now
   otherwise we might get wrong result
"""


def canJump(self, nums: List[int]) -> bool:
    max_reach = 0
    i = 0
    while(i<=max_reach): #notiece we are dynamically updating the index range (no exceeding max_reach)
        max_reach = max(max_reach, i+nums[i])
        if max_reach>=len(nums)-1:
            return True
        i += 1
    return False