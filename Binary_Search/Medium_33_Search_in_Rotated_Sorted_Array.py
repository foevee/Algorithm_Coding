"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).  ==> Means Binary Search

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0   Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3   Output: -1

Solution:
Use sorted binary search (3 pointers: low, high, mid), there are two ways
1) Notcie [low, mid], [mid, high] two half must have one half sorted (ascending) and another half unsorted
        we try to find the sorted half and use it start and end value to compare (with target) and decide how to move pointers
2) (!! & faster) Find the rotation value, and still use the normal binary search method to compare:
        except now we move high, low with the rotation shift (e.g. from (normally) high = mid+1 to (now) high = (mid+1+shift)%len(sums))
        (notice after find the rotation value, we can use another way to do binary search: now we determine target in which sorted half 
          i.e. [0, shifft-1] or [shift, n-1], and do normal binary search in that sorted half)

!! Key point for binary search: choose proper mid to avoid dead loop (i.e. Time Limit Error, TLE)
    when there is mid=low later, we need to set mid = (low+high)//2+1 before, since this way mid is right closer to high
    when there is mid=high later, we need to set mid = (low+high)//2 before, since this way mid is left closer to low
    otherwise the loop might stuck in mid==low or mid==high in each case respectively 
    i.e. low=0, high=0, mid=0 when mid = (low+high)//2, there is always low=mid, so when setting mid=low will lead to dead loop (TLE)

Complexity: Time O(logN), Space: O(1)
"""

### Method 1: Find the sorted half and use it to compare and determine how to move the binary search pointer
### Example: [4,5,6,7,0,1,2]， we need to find the sorted half and use this half to compare target and then decide how to move the pointer
###   if nums[low]=4, num[mid]=6, nums[high]=0, now nums[mid]>=num[low] (<num[high]), so the left half is sorted
###   if nums[low]=6, num[mid]=0, nums[high]=2, now nums[mid]<=num[high] (>num[low]), so the right half is sorted
###   Trick: notcie the corner case here, must consider the sorted half might be all the same, not all strictly ascending, 
###          so we must use the pair of either (a) nums[mid]<=nums[high], nums[mid]>=nums[low]  or (b) nums[mid]<=num[high], nums[mid]>num[high] 
###          we must make sure two situations are complementary

def search(self, nums: List[int], target: int) -> int:
    if not nums: #corner case, list is []
        return -1
    low, high = 0, len(nums)-1
    while(low<high):
        mid = (low+high)//2
        if(nums[mid]==target):
            return mid
        
        #right half is sorted, use this half to compare
        if(nums[mid] <= nums[high]): #!!!Trick: must include = here (use <= not <), corner case all the same (not strictly ascending)
            if(nums[mid] < target <= nums[high]): #target within the left half, so move high=mid-1 (since nums[mid]!=target)
                low = mid+1
            else:
                high = mid-1  #target not within the left half, we can exclude the [low, mid] half, move low=mid+1

        #left half is sorted, use this half to compare
        elif(nums[mid] >= nums[low]): #!!!Trick: must include = here (use >= not >), corner case all the same (not strictly ascending)
            if(nums[low] <= target < nums[mid]): #target within the right half, so move low=mid+1 (since nums[mid]!=target)
                high = mid-1
            else: #target not within the right half, we can exclude the [mid, low] half, move high=mid-1
                low = mid+1
    
    return low if nums[low]==target else -1

### Method 2 (faster): Find the rotated value and move binary search pointers with this rotation shift (for low, high change)
def search(self, nums: List[int], target: int) -> int:
    if not nums:
        return -1
    n = len(nums)
    low, high = 0, n-1
    ##(a) Find the rotation shift value (which is the index of the lowest value)
    while(low<high):
        #notice we want to find the lowest value, which must be in the most left of the sorted half
        #  if we want to find the highest value index, we can not compare by nums[mid]<=nums[high] and move high=mid-1
        #  now we do not know the highest is in the end of the right half (rotation=0) or first half （rotation>0）
        #  instead we should compare by nums[mid]>=nums[low], now whatever rotation is, the highest value index must be no less than mid, so move low=mid
        #in short, we always use the opposite direction to find extreme value index 
        #  i.e. left(low) sorted half for highest value index, right sorted half for lowest value index

        #Plus, we need to avoid the dead loop (by setting mid opposite close to the "mid=.." one): 
        #   when using mid=(low_high)//2, mid is left closer to low, so we can not use low=mid 
        #      (otherwise might never change, deal loop, i.e. low=0, high=1, mid=0 already has mid=low)
        #   when using mid=(low_high)//2+1, mid is right closer to high, so we can not use high=mid 
        #      (otherwise might never change, deal loop, i.e. low=0, high=1, mid=1 already has mid=high)
        #   so when there is "high=mid", set mid=(low+high)//2, while when there is "low=mid", set mid=(low+high)//2+1

        ##(a.1) one way (find the lowest value)
        mid = (low+high)//2 #there is high=mid below, we must use (low+high)//2, which is left closer to low
        if(nums[mid]<=nums[high]): #if the right half is sorted, then the lowest value must no larger than the mid => move high=mid
            high = mid
        else: #use if else to make it complementary (as no direct check on mid now)
            low = mid+1
    shift = low  #notice lowest value index is shift_value (while the highest value index is shift_value-1)

        ##(a.2) Another way (find the highest value)
    #    mid = (low+high)//2 + 1  #there is low=mid below, we must use (low+high)//2+1, which is right closer to high
    #    if(nums[mid]>=nums[low]): #if the right half is sorted, then the lowest value must no larger than the mid => move high=mid
    #        low = mid
    #    else: #use if else to make it complementary (as no direct check on mid now)
    #        high = mid-1
    #shift = low+1  #notice the highest value index is shift_value-1
    
    ##(b.1) Easy Understanding Way: choose target in which sorted half [0, shift-1] or [shift, n-1] and then use normal binary search
    #if (target<nums[-1]) or (rotation==0): #second half or unrotated
    #    #also use nums[-1] instead of nums[0] to include non-rotate situation
    #    low,high=rotation,n-1
    #else:
    #    low,high=0,rotation-1
    #while(low<=high):
    #    mid=(low+high)//2
    #    if(nums[mid]==target):
    #        return mid
    #    if(nums[mid]<target):
    #        low=mid+1
    #    else:
    #        high=mid-1
    #return -1    

    ##(b.2) Better way -- use the normal binary search pointer (low, high), but compare with the real_mid (shifted) value
    low, high = 0, n-1
    ##Normal binary search with shifted move for mid pointer to compare
    while(low<=high):  #we include the low=high for convenience (use loop find real_mid)
        mid = (low+high)//2
        #use shifted real_mid pointer to compare, but low, high still move as normal, when the interval narrows toworads one way, 
        #  the corresponding real_mid also shift the same direction, thus achieving the shifted binary search (still work!)
        #  when low==high (interval narrow to 1), the corresponding nums[real_mid] should == target, otherwise value not found
        #Think of this as a normal interval narrow with an anchor attached to the real value (read_mid) and directed to shift by that
        real_mid = (mid+shift)%n  
        if(nums[real_mid]==target):
            return real_mid
        elif(nums[real_mid]<target): #then the target should be in [real_mid, real_high], we move low=mid+1 to shift [low, high] higher, which corresponds to the real_mid being shifted (higher) then before, thus helping narrow the interval and binary search
            low = mid+1
        else:   #then the target should be in [real_low, real_mid], should be shifted lower, thus use high=mid-1
            high = mid-1
    return -1  #if outside loop without return, means not found one
            
        
        


                
                


        
