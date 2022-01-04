"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 
Constraints:
1 <= m, n <= 100


Solution:
Dynamic Programming: normal use 2D array, optimize to use 1D array only
"""

def uniquePaths(self, m: int, n: int) -> int:
    #can use dynamic programming (loop m*n array), no need recursion otherwise Time Limite Exceeded (stackoverflow)
    #recursion, check from bottom-right, can only move left or up
    
    #Method 1: 2D array
    #dp = [[1 for _ in range(n)] for _ in range(m)] #init since dp[i][0]==dp[0][j]==0
    
    #Method 2 (optimized): 1D array
    dp = [1 for _ in range(n)] #init to 1
    for i in range(1, m):
        for j in range(1, n):
            #dp[i][j] = dp[i-1][j] + dp[i][j-1] #O(M*N) space
            dp[j] = dp[j] + dp[j-1] #Optimized version: O(N) space
    return dp[n-1]
                
    