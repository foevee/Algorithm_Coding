"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Constraints:
0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.


Solution:
The key is to track the matching with '*', we loop through to find the correct matched in string (might be length 0 ~ n) for '*', 
    when encountering *, we track last_star position (for * in pattern) and last_match position (for alpha in string) and keep moving i to find next non-* pattern
    return to normal match of non-* pattern and alphabet in string
    [!!!] once two not matched and we have encountered '*' before, we will restart matching string (j) from last_match + 1 with pattern (i) from last_start + 1
Keep doing so and check if we can reach the end of both strings, also allowing the edge case of remaining unmatched characters in pattern are all '*'

Complexity: O(N) time -> loop through the length of string, O(1) space
"""
def isMatch(self, s: str, p: str) -> bool:
    m = len(p)
    n = len(s)
    i, j = 0, 0
    last_star = -1
    last_match = -1
    while j<n: #pattern criteria used in the loop since we might revisit back
        if i<m and (p[i]=='?' or p[i]==s[j]): #? and alpha case
            i += 1
            j += 1
        elif i<m and p[i]=='*':
            last_star = i
            last_match = j
            i += 1 #only move pattern here
        elif last_star!=-1: #last * match is not successful, start to rematch
            #notice enter here means the non-star character after last * in pattern
            i = last_star + 1
            j = last_match + 1
            last_match += 1
            
        else: #e.g. non-matched alpha case
            return False
    
    while i<m and p[i]=='*': #can only allow remaining pattern be all '*' to match
        i += 1
    return i==m and j==n
    