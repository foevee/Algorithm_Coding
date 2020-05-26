"""
[Facebook Interview Problem]
(This problem is an interactive problem.)
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [m, n], which means the matrix is m * n.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

 

Example 1:
Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:
Input: mat = [[0,0],[0,0]]
Output: -1

Example 3:
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
Complexity: Time O(logN), Space: O(1)


Method:
Since each row is in ascending order, we should track each row from right to left. 
To find the leftmost index, we start tracking a new row's column only from last rows leftmost index (column) - 1, if found less we update
1) One way: In each row, use binary search to search the leftmost index from [0, lest row's leftmost index - 1]
   Complexity: Space O(1), Time < O(M*log(N))  [may not get exact expr], since we are narrowing the column searching range each time (for each row), 
   
2) Another way: In each row, use linear time search from right (last row's leftmost index-1) to left, until we see a value < 1 or reach index = 0
    We only visit each column one time, unlike binary search we might still visit more than once due to the un-continuous jump in pointers (low, high)
    Complexity: Space O(1), Time < O(N), we only visit each column one time, from row=0 (up) to row=m-1 (down), acting like visiting only one row

We might not see method 1) or 2) which is better, since 1) use binary search in each row interval but might discretely jump to  visit same column more than once.
In practice, 2) uses 100 ms while 1) uses 108 ms.


"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


### Method 1 (Binary Search Column): 
### Top to down (row), right to left (column), visit each row and use binary search to find the column in that row to update
def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    m, n = binaryMatrix.dimensions()
    pos = n  #save the left most position (initialized to n, which can never be reached if found 1 in the matrix)
    for i in range(m):
        low,high = 0, pos-1  #always finding new start from last round pos-1
        while(low<=high):  #when we have both case low/high=mid+/-1 (not = mid), we should include low=high (otherwise miss the situation)
            mid = (low+high)//2
            value = binaryMatrix.get(i, mid)  
            if(value==1 and mid<pos):
                pos = mid
                high = mid-1  #notcie even if finding new one, we still need keep finding if there is smaller one
            elif(value<1):
                low = mid+1
            else:
                high = mid-1
            
    return pos if pos<n else -1

### Method 2 (Linear search column): Top to down (row), Right to left (column), visit each row but linearly searching column from the last row's column index
### We can see we only visit each column one time, tracking all the row, the time complexity is O(N) (n is the column number)
def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    m, n = binaryMatrix.dimensions()
    pos = n
    for i in range(m):
        j = pos-1  #always start from last round pos-1 to find new leftmost
        while(j>=0):
            value = binaryMatrix.get(i,j)
            if(value==1):
                pos = j
                j -= 1  #notcie even if finding new one, we still need keep finding if there is smaller one
            elif(value>1):
                j -= 1
            else: #<1
                break #since ascending, we can not find ==1 (when going left)
    return pos if pos<n else -1
            
        
        


                
                


        