"""
Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
which means you can not rob two adjacent house


Method:
Use greedy, each time loop for two situation: rob current house i (then depend on i-2) or do not rob current house i(depend on i-1)
"""

def rob(self, nums):
    if not nums:
        return 0
    if len(nums)<2:
        return nums[0]
    rob=[0 for _ in range(len(nums))]
    notrob=[0 for _ in range(len(nums))]
    rob[0],notrob[0]=nums[0],0
    rob[1],notrob[1]=nums[1],rob[0] #need to make sure len(nums)>=2
    for i in range(2,len(nums)):
        rob[i]=nums[i]+max(notrob[i-2],rob[i-2])
        notrob[i]=max(rob[i-1],notrob[i-1])
    return max(rob[-1],notrob[-1])