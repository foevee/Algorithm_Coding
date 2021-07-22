"""
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.
You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.


Example 1:
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

Example 2:
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 103
m <= n <= 105
-1000 <= nums[i], multipliers[i] <= 1000


Method:
Use a dynamcial programming to loop m operations and each possible combinations (using first starting l elements and thus last m-l elements)
At each score[oper_i][l], we calculate the ith operation using first l elemts from nums (and thus last m-l elements of nums)
It will be connected to the oper_i-1 th operation, and the oper_i th operation should either from (a) the lth element (choose from start) or (b) from the n-(oper_i-l) th element (choose from end)


Notice we have two ways below:
One is original 2D (m*m) array
Another is the optimized 2*m array way (iteratively using 2 rows only)---> faster in space

"""

def maximumScore(self, nums: List[int], muls: List[int]) -> int:
    m, n = len(muls), len(nums)
    MIN_VAL = float('-inf')
    
    #1. original, 2D array of m*m (notice if init n*m will TLM (time limit error)), we only need score[m][m] indeed (since l<=oper_i<=m below)
    score = [[0 for _ in range(m+1)] for _ in range(m+1)]        
    
    #2. optimized way, only 2 rows --- update iteratively using 2 rows (will not conflict)
    #score = [[0 for _ in range(n+1)] for _ in range(2)]
    #row_id = 1
    
    #loop through m operations (index from 1)
    for oper_i in range(1,m+1): 
        #row_id = 1-row_id
        
        #loop through the starting index of nums oper_times, means using first l elemets of nums, thus last m-l elements of nums
        #for the score of using lth (1-indexed), choose the current/lastest from the last of nums (nums[]) or start of nums (nums[l-1])
        for l in range(oper_i+1): 
            #2D way --- too many memory -- TLE
            start = score[oper_i-1][l]+nums[n-oper_i+l]*muls[oper_i-1] if l<oper_i else MIN_VAL  #a. use the end point of nums
            end = score[oper_i-1][l-1]+nums[l-1]*muls[oper_i-1] if l>=1 else MIN_VAL   #b. use the start point of nums
            score[oper_i][l] = max(start, end)
            
            
            #optimized way -- update only using 2 row (since we will not use this new updated array until last round, won't conflict)
            #start = score[1-row_id][l]+nums[n-oper_i+l]*muls[oper_i-1] if l<oper_i else MIN_VAL  #a. use the end point of nums
            #end = score[1-row_id][l-1]+nums[l-1]*muls[oper_i-1] if l>=1 else MIN_VAL #b. use the start point of nums
            #score[row_id][l] = max(start, end)
    
    return max(score[m])
        
                
            