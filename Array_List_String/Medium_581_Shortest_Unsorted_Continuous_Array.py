'''
Given an integer array, you need to find one continuous subarray 
that if you only sort this subarray in ascending order, 
the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

'''

#1. Sort the array and compare to the original one 
# (most left unmatched  -  most right unmatched)
def findUnsortedSubarray(self, nums):
    nums_sort=sorted(nums)
    left=right=-1
    n=len(nums_sort)
    for i in range(n):
        if nums_sort[i]!=nums[i]:
            if left==-1:
                left=i
            else:
                right=i #can not break early, must loop till the end (in case match in between)
        
    return right-left+1 if right!=left else 0 #in case both =-1, unchanged (then not +1)
            
#2. Use Min-Max window
# besides this window, all element less than current max (from right), larger than current min (from left)
# first we save the current max (from right), current min (from left), then use this to compare the array
def findUnsortedSubarray(self, nums):
    #min-max reference (for each step)    
    n=len(nums)
    if(n<=1):
        return 0
    curr_max,curr_min=[0]*n,[0]*n
    max_=nums[0]
    min_=nums[-1]
    i=n-1
    while(i>=0): #save current min from the end to begining
        min_=min(min_,nums[i])
        curr_min[i]=min_
        i-=1
    i=0
    while(i<n):
        max_=max(max_,nums[i]) #save current max from the begining to the end
        curr_max[i]=max_
        i+=1
    
    i=0
    left=right=-1
    while(i<n): #left unmatched, num[i] is not current min (larger than later elem)
        if(nums[i]<=curr_min[i]):
            i+=1   
        else:
            left=i
            break
    i=n-1
    while(i>=0): #right unmatched, num[i] is not current max (less than previous elem)
        if(nums[i]>=curr_max[i]):
            i-=1
        else:
            right=i
            break
    return right-left+1 if left!=right else 0
