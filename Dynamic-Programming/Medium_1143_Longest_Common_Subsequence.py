"""
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.


Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:
1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

Solution:
Use dynamic programming to loop through two text strings
  Save the longest common array num at index i, j (i in text1, j in text2) in the longest array
  For longest[i][j], its longest num is from the maximum between (1)longest[i-1][j] (2)longest[i][j-1] (3)longest[i-1][j-1]+int(text1[i]==text2[j])
  Notice we do not only update (i,j) using (i-1,j-1)+current value if equal, but also use (i-1,j) and (i,j-1)

Complexity: Time O(M*N) Space O(M*N)
"""


def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m, n = len(text1),len(text2)
    longest = [[0 for j in range(n)] for i in range(m)]
    ## initialize (always notice boundary)
    for i in range(m):
        longest[i][0] = 1 if (text2[0] in text1[:i+1]) else 0
    for j in range(n):
        longest[0][j] = 1 if (text1[0] in text2[:j+1]) else 0
        
        
    for i in range(1,m):
        for j in range(1,n):
            curr = 1 if text1[i]==text2[j] else 0
            value = longest[i-1][j-1]+curr
            ## max from array[i-1][j], array[i][j-1], array[i-1][j-1]+int(text[i]==text2[j])
            longest[i][j] = max(longest[i-1][j], longest[i][j-1], value)
        
    return longest[m-1][n-1]