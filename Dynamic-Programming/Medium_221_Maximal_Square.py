"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4

Method:
Use dynamic programming, update the max square size (including the current one and the left-up directions) at step from top left to bottom right
  at each step, count if current value is 1 (since our counts include the current value)
      if curr = '0', then update the array with 0 (current is not 1 so the continous max square include current one is 0)
      if curr = '1', then count the min "max-square-size" of the left-up directions (3 values, (i,j-1), (i-1,j), (i-1,j-1)), update by this min + 1
         notice we take min since as long as one direction has value less than this, we can not get a full 1 square (thus can not extend the size by +1)
  we use this array to track the max square size including the current step's value (otherwise we can not get continuous track, can not extend by +1)
  and use another max_value to track the real max value as a whole (might not include current one)
Complexity: Time O(M*N), Space O(M*N)

To optimize:
we only need to remember two rows at each step (i.e. (i,j), (i-1,j), (i,j-1), (i-1,j-1)), so we can create an array of 2*N size
Complexity: Time O(M*N), Space O(2*N)
"""


def maximalSquare(matrix: List[List[str]]) -> int:
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    #save current max square size, must include current one, if current matrix is 0, then this is 0
    currMaxSquare = [[0 for j in range(n)] for i in range(m)] 
    max_square = 0
    for i in range(m):
        for j in range(n):
            if (i==0 or j==0):
                currMaxSquare[i][j] = int(matrix[i][j])  #count only single value (1 or 0)
            else:
                currMaxSquare[i][j] = int(matrix[i][j]) #initialize to current count (1 or 0)
                last_value = min(currMaxSquare[i][j-1], currMaxSquare[i-1][j], currMaxSquare[i-1][j-1])
                if(int(matrix[i][j])): #if current=1, add the min value of three left-up currMaxSquares
                    currMaxSquare[i][j] += last_value
                    
            max_square = max(currMaxSquare[i][j], max_square)
    
    #return the full number of the max square (need **2)
    return max_square**2
                    
                    