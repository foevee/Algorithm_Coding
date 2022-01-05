"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.

Solution: Backtrack:
    loop i for 0 to n-1, if str[0:i+1] is palindrome, then backtrack (recursion) remaining str[i+1:]
    when backtrack string length=0, add path to final result and return

Time complexity: O(n*(2^n))
  For a string with length n, there will be (n - 1) intervals between chars.
  For every interval, we can cut it or not cut it, so there will be 2^(n - 1) ways to partition the string.
  For every partition way, we need to check if it is palindrome, which is O(n).
  So the time complexity is O(n*(2^n))

  Roughly,
  T(n)=T(n-1)+T(n-2)+..+T(1)  ---> for loop i in [0,n), each partition to further bactrack T(n-i)
  T(n+1)=T(n)+T(n-1)+..+T(1)
  T(n+1)=2T(n)
  T(n)=2^n

Complexity: Time O(n*(2^n)), Space: O(n*(2^n))---> same, 2^n partitioning, each yield one list of at most n size
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final, path = [], []
        self.backtrack(s, final, path)
        return final
    
    def ispalindrome(self, s):
        i, j = 0, len(s)-1
        while i<j:
            if s[i]!=s[j]: return False
            i, j = i+1, j-1
        return True
        
    def backtrack(self, s, final, path):
        n = len(s)
        if n==0: 
            final.append(path)
            return
        
        for i in range(0,n):
            substr = s[:i+1]
            if self.ispalindrome(substr): 
                self.backtrack(s[i+1:], final, path+[substr])


                
                


        
