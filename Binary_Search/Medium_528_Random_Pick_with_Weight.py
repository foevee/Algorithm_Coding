"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Example 1:
Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:
Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]


Explanation:
The problem is, we need to randomly pick an index proportional to its weight.
We have weights array, each weights[i]  represents weight of index i. 
The more the weight is, then high chances of getting that index randomly.

say we have the numbers 1, 5, 2 easiest solution is to construct the following array
arr[] = {0,1,1,1,1,1,2,2}
then generate a random number between 0 and 7 and return the arr[rnd]. This is solution is not really good though due to the space requirements it has (imagine a number beeing 2billion).

The solution here is similar but instead we construct the following array (accumulated sum)
{1, 6, 8} generate a number between 1-8 and say all numbers generated up to 1 is index 0. All numbers generated greater than 1 and up to 6 are index 1 and all numbers greater than 6 and up to 8 are index 2. After we generate a random number to find which index to return we use binary search.


Method: Uniform Sampling
We can use uniform distribution to sample a specific distribution
For a specific distribution (as here denoted by weight), the inverse of its cdf is always the uniform function.
So we can use its cdf inverse with uniform distribution to generate this specific distributiion

- We first generate the cdf of this distribution by simply cumsuming the weights each index, seting the max cumsum as n. 
(We omit standardize the cumsum to real cdf here as integers are more convenient for later binary search and compare. If divided by the sum of all weights, then the cumsum will become real cdf (0~1)).
- Then we simulate an uniform integer within the range of 1~n (both inclued) using random.randint. 
- Using binary search, we can find where this random int belongs in the cumsum list
  i.e. cumsum[i-1]<rand_int<=rand[i], then we return the index i

This is indeed trying to simulate the index following the inverse of its weights cdf, starting from uniform randint and reverse back to find the index by binary search the index integral this rand_int belongs. This makes senses since the larger the weight, the larger the integer range of the interval (since cumsum[i]-cumsum[i-1]=weight[i]), and thus the higher chance of this index being chosen.

Complexity: Time O(N + logN) Space O(N)

"""

import random
class Solution:

    def __init__(self, w: List[int]):
        self.cumsum = [w[0]]  #cumsum if indeed the cdf of this distribution (not standardized)
        for i in range(1,len(w)):
            self.cumsum.append(self.cumsum[-1]+w[i])

    def pickIndex(self) -> int:
        max_ = self.cumsum[-1]
        # from 1 to max_ (included) uniformly divide max_ parts since 1~max_ has max_ numbers (start from 0 will get one extra (max_+1))
        rand = random.randint(1,max_) #1<=rand<=max_ (equal to random.randrange(1,max_+1))
        low, high = 0, len(self.cumsum)-1
        
        while(low<high): #use binary search to find the index interval this rand belongs (cumsum[i-1]<rand<=cumsum[i], return i)
            mid = (low+high)//2
            if rand > self.cumsum[mid]:
                low = mid+1
            else:
                high = mid
        return low
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()