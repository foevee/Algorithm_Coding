"""
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 
Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


Solution:
Use loops for 2 times, 
    first search the zero index and record its row and column, 
    second loop set item in those row or column to be 0
    
Two methods: 1) save row and column in a set, use O(M+N) extra space; 2) save row and column in the first row & first column item, in place, use O(1) extra space
"""

# Method 1: O(M+N) extra Space, O(M*N) Time
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zeros = set()
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if(matrix[i][j]==0): 
                zeros.add(str(i)+'_') #row i
                zeros.add('_'+str(j)) #col j
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0: continue
            if (str(i)+'_' in zeros) or ('_'+str(j) in zeros):
                matrix[i][j] = 0
                    
# Method 1: O(1) extra Space, O(M*N) Time     
# First natural loop, second reverse loop to avoid changing first row/col reference in advance, thus might affect later i>0m j>0 row/col references
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """    
    m, n = len(matrix), len(matrix[0])
    col0, row0 = False, False
    for i in range(m):
        for j in range(n):
            if(matrix[i][j]==0): 
                #set the first element of this row and column to be 0 
                #when i=j=0, need to distinguish from row 0 or col 0 (otherwise affect non-zero items to be zero)
                matrix[i][0] = 0
                matrix[0][j] = 0
                if i==0: row0 = True
                if j==0: col0 = True
                    
    
    #use revser loop, so that first row and first column will only be changed last, won't affect reference to other rows/cols
    for i in range(m-1,-1,-1):
        #extra check for row0 in case matrix[0][0] from col0 only
        if i==0 and row0==False: continue 
        for j in range(n-1, -1, -1):
            if matrix[i][j]==0: continue   
            #extra check for col0 in case matrix[0][0] from row0 only
            if j==0 and col0==False: continue
            #for i=j=0 case, both [i][0] and [0][j] are the same, need check their 0 source (from col or row, as extra check above)
            if matrix[i][0]==0 or matrix[0][j]==0:                    
                matrix[i][j] = 0
        
        