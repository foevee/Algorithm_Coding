"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Solution: Use Dynamic Programming

To apply DP, we define the state dist[i][j] to be the minimum number of operations to convert word1[0..i) to word2[0..j), using the fist i or j words, index from 0 to i-1 or 0 to j-1 (included)

For the base case, that is, to convert a string to an empty string, the mininum number of operations (deletions) is just the length of the string. So we have dist[i][0] = i and dist[0][j] = j.

1) For the general case to convert word1[0..i) to word2[0..j), we break this problem down into sub-problems. Suppose we have already known how to convert word1[0..i-1) to word2[0..j - 1) (dist[i - 1][j - 1]), if word1[i-1] == word2[j-1], then no more operation is needed and dist[i][j] = dist[i-1][j-1].

2) If word1[i - 1] != word2[j-1], we need to consider three cases.
- Replace word1[i-1] by word2[j-1] (dist[i][j] = dist[i-1][j-1] + 1)
- Delete word1[i-1] (dist[i][j] = dist[i-1][j] + 1) as word1[0..i-1) = word2[0..j), which is implied in dist[i-1][j] (already covered)
- Insert word2[j-1] to word1[0..i) (dist[i][j] = dist[i][j-1] + 1) as word1[0..i) = word2[0..j-1), which is implied in dist[i][j-1] 
So when word1[i-1] != word2[j-1], dist[i][j] will just be the minimum of the above three cases.

Complexity: Time O(M*N) Space O(M*N)
"""

def minDistance(word1, word2):
    """Dynamic programming solution"""
    m = len(word1)
    n = len(word2)
    #dist[i][j] is the # of operations to match word1[0...i) to word2[0...j), which already covered the match of two
    dist = [[0] * (n + 1) for _ in range(m + 1)]
    

    for i in range(m + 1):
        dist[i][0] = i
    for j in range(n + 1):
        dist[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]: #1) the new character matched, do not need operate more (use distance[i-1][j-1])
                dist[i][j] = dist[i - 1][j - 1]
            else: 
                #2) if new character not match, take the minimum of these three cases and add 1 more operation
                #delete last in word1(i-1,j), insert last in word1 (i,j-1), replace last in word1 (i-1,j-1)
                dist[i][j] = 1 + min(dist[i - 1][j], dist[i][j - 1], dist[i - 1][j - 1])
    
    return dist[-1][-1] #the last dist[m][n] is the # of operations to convert word1 to word2