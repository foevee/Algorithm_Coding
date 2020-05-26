"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1


Method:
Use a dynamcial programming to loop through the original matrix (2d array)
At each matrix[i][j], choose the element as the right-bottom one and count its left-top three directions value
do the following check only for i>=1 and j>=1 (not including the first row/column since they have at most 1 square)
  if the current i,j is 1, take the min of the three left top values and add + 1
  if not, just take the current matrix[i][j] value as the new value (which is 0)


"""

def countSquares(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    result = 0
    for i in range(0,m):
        for j in range(0,n):
            #only count larger square (top-left dir) when curr matrix[i][j]==1
            if matrix[i][j] and i>=1 and j>=1: 
                matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
            result += matrix[i][j]
    return result