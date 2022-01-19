"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?

Solution: DFS, BFS, DP (2D array), DP (1D array)
"""
#Method 1: DFS with memorization (if no memorization then will TLE - stack overflow)
#Time O(M*N), Space O(N)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        if m+n!=p: return False
        visited = set()
        return self.dfs(s1, s2, s3, 0, 0, visited)
    
    #DFS must add memorization, otherwise TLE (stack overflow)
    def dfs(self, s1, s2, s3, i, j, visited):
        #first check if reaching end
        if i+j==len(s3): return True
        
        #then check if already visited (which means not reaching end from this path before, so false)
        #unique way to encode and save path (only use one num),
        path_encode = i*len(s2+1)+j  #add extra 1 since i~[0,len(s1)], j~[0,len(s2)], otherwise (1,0) duplicates with (0,len(s2))
        if path_encode in visited:
            return False
        visited.add(path_encode)

        way1, way2 = False, False
        if i<len(s1) and s1[i]==s3[i+j]: way1 = self.dfs(s1,s2,s3,i+1,j, visited)
        if j<len(s2) and s2[j]==s3[i+j]: way2 = self.dfs(s1,s2,s3,i,j+1, visited)
        return way1 or way2

        

#Method 2: BFS with memorization
#Time O(M*N), Space O(M*N)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        if m+n!=p: return False
        
        #BFS, loop through all combs of (x, y) of s1 and s2, check visited (x, y) combs to avoid furture re-visit
        stack = [(0,0)] #init x, y to be 0
        visited = set((0,0))
        while stack:
            x, y = stack.pop(0)
            if x==m and y==n: return True #reach end
            visited.add((x,y))
            #BFS add two ways - match next x in s1 or next y in s2
            if x<=m-1 and s1[x]==s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1,y))
                visited.add((x+1,y))
            if y<=n-1 and s2[y]==s3[x+y] and (x, y+1) not in visited:
                stack.append((x,y+1))
                visited.add((x,y+1))
        return False
        
        


#Method 2: Dynamic Programming - 2D array
#Time O(M*N), Space O(M*N)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        if m+n!=p: return False
        dp = [[True for _ in range(n+1)] for _ in range(m+1)]
        
        #init boundary line, using only one string
        for i in range(1, m+1): #notice index for s1,s2,s3 should be idx-1
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1] #must have prev substr match and current one match
        for j in range(1, n+1):
            dp[0][j] = dp[j-1] and s2[j-1]==s3[j-1]
        
        for i in range(1,m+1):
            for j in range(1, n+1): 
                #two matching ways, check if either one is true
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
                
        return dp[m][n]


#Method 3: Dynamic Programming - 1D array
#Modify the logic from 2D DP way bove
#Time O(M*N), Space O(N)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        if m+n!=p: return False
        dp = [True for _ in range(n+1)]
        
        #Optimized way: only init for dp[0][j] and s2, leave dp[i][0] and s1 within the loop as dp[0]
        for j in range(1, n+1):
            dp[j] = dp[j-1] and s2[j-1]==s3[j-1]
        
        
        for i in range(1,m+1):
            #the dp[i][j-1] in 2D way need init dp[i][0] when j=1, this hasen't been init before
            dp[0] = dp[0] and s1[i-1]==s3[i-1]
            for j in range(1, n+1): 
                #optimized way (2D dp to 1D)
                dp[j] = (dp[j] and s1[i-1]==s3[i+j-1]) or (dp[j-1] and s2[j-1]==s3[i+j-1])
        
        return dp[n]

    