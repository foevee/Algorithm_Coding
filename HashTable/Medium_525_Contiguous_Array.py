"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.


Solution [hashmap]:
We use a dictionary to count the number of 0 and 1 of current step,
If meeting 0 count-=1, elif meeting 1 count+=1
Thus for an countiguous array of equal number of 0 and 1, its count total = 0 (equal num of -1 and 1)
If at index i and j both have count k, then k - k = 0, and array[i+1:j+1] has equal number of 0 and 1

We use a dictionary to track the contiguous count of each step,
   with key set as the "count" number, and the value set as the earliest index of this count number 
   initializing it with key=0 and value=-1(index) => for later substraction count
(note we only save the earliest index to help get the max diff of index under the same count number)
At each step (i), we update the count number (+/-1) and check if this count number appeared in the dict before
   if it appeared, we update max_len by max(max_len, i-dict[count]) (note we only update max_len but not dict, to keep the earliest index)
   if it not appeared before, we update the dict by dict[count]=i
return max_index which is the largest array length of equal number of 0 and 1
"""


def findMaxLength(self, nums: List[int]) -> int:
   ##save a hash map to track the count of 0 (if 0 count-=1) and 1(if 1 count+=1) at current step
   track_count = {0:-1} #initialize count=0 with index -1 (otherwise can not substract and get count number properly)
   max_len = 0
   count = 0
   for i in range(len(nums)):
      if nums[i]==0:
         count += -1
      elif nums[i]==1:
         count += 1
      ##track if the current count number in dictionary
      if count in track_count:
         max_len = max(max_len, i-track_count[count])  #length is the diff between two index of same count
      #if already in dict, not update, so we always save the earliest index for this count
      else:
         track_count[count] = i #save the index for each count number
                
   return max_len