"""
Given an array of integers and an integer k
Find the total number of continuous subarrays whose sum equals to k.


Method:
1. Key: cumsum[j]-cumsum[i]==k, calculate the cumsum at each step while save it into dict "countsum", 
   using the difference between two cumsum (== k) to find array
2. Doing the loop to calculate the cumsum, count the diff==k number, and update the dict
   In this way, while counting, the "countsum" only include the index before, we will maintain the j>i index (latter - before)
   Thus we will not have the cumsum[i]-sumsum[j]==k (i<j) error and count wrong!
   [ke]
3. Note: must find array first (check countsum[cumsum-k]) then update current cumsum into key (countsum[cumsum]++)
   otherwise might include current cumsum into count and get repeating count (when k==0)
"""


def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    cumsum=count=0
    countsum={0:1} #add one padding for i=-1, since cumSum[j]-cumSum[i] will not include i, and we need to include i=0 scenario
    for val in nums:
        cumsum+=val
        #for subarray(i,j), cumSum[j]-cumSum[i]==k, find each combination of i from countSum[key], j from countSum[val+k]
        count+=countsum.get(cumsum-k,0) #in case cumSum-k not appeared before
        #Note!! first count then uodate, otherwise will include itself
        countsum[cumsum]=countsum.get(cumsum,0)+1 #dict.get(key,option_val), if key not appeared then get option_val
    return count