from random import randint
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        Using Quick Sort Method, decrease the Time complexity to O(N)
        """
        def partition(l, r):
            #Choose a random number as pivot and set it to the right (nums[r])
            ri = randint(l, r)
            nums[r], nums[ri] = nums[ri], nums[r]
            for i, v in enumerate(nums[l: r+1], l):
                if v >= nums[r]: #Here nums[r] are pivot, unchanged
                    #change into descending order
                    nums[l], nums[i] = nums[i], nums[l] #swap between left and the current
                    l += 1
            #the above loop already include put nums[r](pivot) to its rights place
            #that is
            #nums[l], nums[r] = nums[r], nums[l]
            return l
        
        l, r, k = 0, len(nums) - 1, k - 1
        while True:
            pos = partition(l, r)
            if pos < k:
                l = pos + 1
            elif pos > k:
                r = pos - 1
            else:
                return nums[pos]
