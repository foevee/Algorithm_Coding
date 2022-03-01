"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

"""
#Method 1: Loop through the array and discuss situation according to digit or alpha or '[' or ']'
#Time: O(N), Space: O(N)
class Solution:
    def decodeString(self, s: str) -> str:
        i, n = 0, len(s)
        result = ""
        stack = [] #use one stack to save both num and string, guaranteed 2i is num, 2i+1 is string
        currnum = 0
        currstr = ""
        for i in range(n):
            if s[i].isalpha(): #can directly add to currstr
                currstr += s[i]
            
            elif s[i].isdigit():
                currnum = currnum*10+int(s[i])
                
            elif s[i]=='[': #save currstr, currnum and reinitialize
                stack.append(currstr) #str before '['
                stack.append(currnum) #num for str within '[]'
                currstr = ""
                currnum = 0
            
            elif s[i]==']':
                #pop order need align with append order (reversely)
                num = stack.pop(-1)
                prevstr = stack.pop(-1) #might pop out as "" (empty stack)
                currstr = prevstr + currstr*num #re-init currstr as prevstr + curr(k*[str within])
            

        return currstr

#Method 2: recursion
#since each num must outside "[]", we read num and use recursion to decode string within '[]'
# also need to return index position of looped ']' so next around starts there
#Time: O(N), Space O(1)
class Solution:
    def decodeString(self, s: str) -> str:
        return self.decodeRecursion(s, 0)[1]
    
    def decodeRecursion(self, s, i):
        n = len(s)
        result = ""
        while i<n and s[i]!=']': #only count towards string with nearest '[]'
            if s[i].isalpha():
                while i<n and s[i].isalpha():
                    result += s[i]
                    i += 1
                
            elif s[i].isdigit():
                num = 0
                while i<n and s[i].isdigit():
                    num = int(s[i]) + num*10
                    i += 1
                
                i += 1 #for '[', skip
                pos, string = self.decodeRecursion(s, i)
                i = pos+1 #for ']', skip
                result += num*string
                
        return i, result #i is the ']' position