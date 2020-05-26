"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.
Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
Return the maximum number of connecting lines we can draw in this way.
 

Example 1:
Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:
Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3

Example 3:
Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:
1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000

Method:
Use Dynamic programming to loop through the array and update the current dp[i][j] according to dp[i-1][j], d[i][j-1], dp[i-1][j-1]
dp[i][j] means the maximum cross-lines up to using the first i elements of A and first j elemets of B
Complexity: Time O(N^2) Space O(N^2)

To optimize, we can use a 1-d array dp[i] to save but still loop for 2-d 
(but need the trick to do backward loop and then forward loop inside for looping B[j]! [see below])
Complexity: Time O(N^2) Space O(N)
"""

## Method 1: Loop by 2D array dp[m][n]
def maxUncrossedLines(A: List[int], B: List[int]) -> int:
    m, n = len(A), len(B)
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            #the index of A,B are one digit lag
            #int(A[i-1]==B[j-1]) decides whether to add+1
            #when A[i-1]==B[j-1] and taking the line, must inherit from i-1,j-1 in case cross-line
            dp[i][j] = max(dp[i-1][j-1]+int(A[i-1]==B[j-1]), dp[i-1][j],dp[i][j-1])  
    return dp[m][n]

## Method 2: Loop by 1D array init to the column length dp[n]
## Looping first by len(A)=m, at each A[i], inside loop by two parallel of B[j]
## 1) First backward loop B (from n to 1) to check if curr A[i-1]==B[j-1] (index of A,B is lagged one), if it is then add dp[j]=B[j-1]+1
##   Notice back-loop helps to use dp[j-1] (which is dp[i-1][j-1]) to update before actually updating it (which will change to dp[i][j-1])
## 2) Then forward loop B to update each step dp[i] using max(dp[i],dp[i-1])
##   in which each dp[j-1] is indeed dp[i][j-1] and dp[j] is indeed max(dp[i-1][j-1]+int(A[i-1]==B[j-1]), dp[i-1][j])
## This way, dp[i] are udpated the same as the 2-d array.

def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
    m, n = len(A), len(B)
    dp = [0 for i in range(n+1)]
    for i in range(1,m+1):
        for j in range(n,0,-1):
            if A[i-1]==B[j-1]:
                dp[j] = dp[j-1] + 1
        for j in range(1,n+1):
            dp[j] = max(dp[j], dp[j-1])
    return dp[n]
                