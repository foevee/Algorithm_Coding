"""
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)


Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:
1 <= stones.length <= 30
1 <= stones[i] <= 1000


Solution:
Use a priority queue to save the data to maintain the max-heap order
each time pop out the largest two values and pop back their difference back to the queue
in the end we left with one element, whic is the weight result

Notice that in Python, we use heapq (by default sort by min-heap), so we need to turn original data to minus sign (-) 
to make the min-heap act like max heap for the original data, in this process we maintain the negative sign and get negative back in the end (take abs or add another -)
"""

import heapq
def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-x for x in stones] #reverse to make min-heap to max-heap for original stones
    heapq.heapify(stones)  #by default, heapify is min-heap
    while(len(stones)>1):
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)
        heapq.heappush(stones, x-y)  #we need to remain x-y (min-second min) to get negative 
        #thus min heap sort will act like max heap for original item in stones
      
    return abs(stones[0])  #equivalent to -stones[0] since we always maintain the negative