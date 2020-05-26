"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

Method:
Simply using the sliding window template, just notice the result/return condition as
  counter==0 and end-start==len(s1)

"""
import collections
def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1)>len(s2):
        return False
    count_dict = collections.Counter(s1)
    begin, end = 0,0
    counter = len(count_dict)
        
    while end<len(s2):
        c = s2[end]
        if c in count_dict:
            count_dict[c] -= 1
            if count_dict[c]==0:
                counter -= 1
        end += 1
        while counter==0:
            c_ = s2[begin]
            if c_ in count_dict:
                count_dict[c_] += 1
                if count_dict[c_]>0:
                    counter += 1
            if end-begin==len(s1): #means find one permutation (when hashmap matched and also the window has the same length as s1)
                return True
            begin += 1
                
    return False