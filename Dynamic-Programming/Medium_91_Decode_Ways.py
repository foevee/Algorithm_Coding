"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.
 

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 
Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

Solution:
From Recursion to Dynamic Programming
see https://leetcode.com/problems/decode-ways/discuss/30451/Evolve-from-recursion-to-dp
"""

## Method 1: original recursion (TLE: not passed test)
## Time: O(2^n): since f(n)=f(n-1)+f(n-2), f(0)=f(1)=1, f(2)=2, fibonacci series, asymptotically O(2^n), but the real tight bound is ~O(1.6^n)
## Space: O(1), no extra array needed


class Solution:
    def numDecodings(self, string: str) -> int:
        return self.recursion(string, 0) if len(string)>0 else 0
    
    def recursion(self, string, i):
        n = len(string)
        #here we only count 1 when reaching all the way to the end, otherwise if counted during process, might overcount as some path may not valid reaching end
        if i==n: return 1 #reach end means get 1 way decoded (notice string="" is excluded in numDecoding function)
        if string[i]=='0': return 0 #no way to decode '0x'
        #way 1
        count = self.recursion(string, i+1) #s[i] is decoded seperately
        if i<n-1 and ((string[i]=='1') or (string[i]=='2' and string[i+1]<'7')):
            #way 2, s[i:i+1] decoded as one number
            count += self.recursion(string, i+2)
        return count

## Method 2: recursion with memorization
## Time: O(n): since we visit each i only once, once got its count number, we save down and use direct reference later
## Space: O(n)

class Solution:
    def numDecodings(self, string: str) -> int:
        n = len(string)
        counted = [-1]*(n+1) #used to memorized recursioned results
        #init last index counted[n] to be 1 since now equal to recursion i==n (return 1), meaning 1 decoding way is found for whole string
        counted[n] = 1
        return self.recursion(string, 0, counted) if n>0 else 0
    
    def recursion(self, string, i, counted): 
        n = len(string)
        if counted[i]!=-1: return counted[i]
        if string[i]=='0': 
            counted[i] = 0
            return 0 #no way to decode '0x'
        #way 1
        count = self.recursion(string, i+1, counted) #s[i] is decoded seperately
        if i<n-1 and ((string[i]=='1') or (string[i]=='2' and string[i+1]<'7')):
            #way 2, s[i:i+1] decoded as one number
            count += self.recursion(string, i+2, counted)
        counted[i] = count
        return count


## Method 3: dynamic programming: 
## we re-write the recursion with memory (method 2) logic to dp, which is indeed loop from the end to beginning
## Time: O(n), Space: O(n)
class Solution:
    def numDecodings(self, string: str) -> int:
        n = len(string)
        dp = [-1]*(n+1)
        dp[n] = 1 #init end (means find one way to end end valid for all)
        #loop back as in recursion logic (only return from end and recursion back)
        for i in range(n-1, -1, -1):
            if string[i]=='0': #no way to start with '0' to decode
                dp[i]=0
                continue
            #way 1: count str[i] as one decoded
            dp[i] = dp[i+1]
            
            #way 2: count str[i:i+2] as one decoded
            if i+2<=n and (string[i]=='1' or (string[i]=='2' and string[i+1]<'7')):
                dp[i] += dp[i+2] #add way 2 only on certain conditions
        
        return dp[0]

## Method 4: dynamic programming with constant space
## following method 3, swe use only two variable to track dp[i+1] and dp[i+2], thus saving memory space
## Time: O(n), Space: O(1)
class Solution:
    def numDecodings(self, string: str) -> int:
        n = len(string)
        #for counting dp[i], use O(1) variables to track dp[i+1] and dp[i+2]
        next_, next2_ = 1, 1
        
        #loop back as in recursion logic (only return from end and recursion back)
        for i in range(n-1, -1, -1):
            if string[i]=='0': #no way to start with '0' to decode
                next2_ = next_
                next_ = 0 #which is curr
                continue
            
            #way 1: count str[i] as one decoded
            curr = next_
            
            #way 2: count str[i:i+2] as one decoded
            if i+2<=n and (string[i]=='1' or (string[i]=='2' and string[i+1]<'7')):
                curr += next2_ #add way 2 only on certain conditions
            
            next2_ = next_
            next_ = curr
            
        return next_