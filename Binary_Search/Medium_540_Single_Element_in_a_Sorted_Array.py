"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.


Method:
According to the O(log n) requirement and O(1) space, we should use binary search.
Since the array is of all twice pair numbers except one, it has the form of (a,a), (b,b),(...),..all pair...(m,m), n, (o,o),(...)...  
  All pair of numbers except single value n. And the n can only happen in the even index.
  So before n, all nums[2*i]==nums[2*i+1] (i=0,1,2...), after n this equation does not hold   (due to order interrupted)
  
  We can discuss the mid pointer position depending on its index off or even:
    1) if mid is odd (mid%2==1): then nums[mid]==nums[mid-1] means mid is <n (before the single value), since mid is only in the even index and mid now is odd (and not included), then we should move low = mid+1; if not equal, then mid is >=n, since mid is only in the even index (can not in mid now), move high = mid-1
    2) if mid is even (mid%2==0): then nums[mid]==nums[mid+1] means mid is <n (before the single value), since mid is only in the even index and mid now is even (but not included), we should move low = mid+2; if not equal, then mid is >=n, since mid is only in the even index (can in mid now), move high = mid
  Then we can move the low, high pointers according to the mid situation and exit the loop when low>=high and take nums[low] as the result
  

Complexity: Time: O(logn), Space: O(1)

"""


### Binary Search, discuss the nums[mid] situation according to the mid index position -- even or odd
def singleNonDuplicate(self, nums: List[int]) -> int:
    if not nums:
        return
    low,high = 0, len(nums)-1
    while(low<high):   #notice not overlapped (otherwise get trapped in loop)
        mid = (low+high)//2
        ## Notice the single value must be in the even index
        if mid%2: #mid is odd index
            if nums[mid]==nums[mid-1]:  #single value > mid and not included (since mid is odd, must +1)
                low = mid+1
            else:                       #single value < mid (since mid is odd, must -1)
                high = mid-1
        else:  #mid is even index
            if nums[mid]==nums[mid+1]: #single value > mid and not included (since mid is even, must +2)
                low = mid+2             
            else:
                high = mid             #single value <= mid(mid is even, must =)
    return nums[low]

        
        


                
                


        