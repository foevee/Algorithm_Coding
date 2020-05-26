"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.



Method: (Sliding window with result checking using "if window size <= min window length" and updating)
Construct a sliding window of two points start, end, name the checking string sstr as string2, the finding string tstr as string1

a.The general logic: use a [start, end] two pointers to denote a window
  for each fixed start, keep moving end pointer +1 till the current window could match the string2
  once the window get matched, move the start pointer +1 as a new start, and then move end to find a new window given this new start

b.Specific Step:
Please see the Medium 438 problem or the Sliding Window Template

Complexity: O(N+K), Space: O(K) (K is the size of hashmap)
"""


## The template way
def minWindow(self, sstr, tstr):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(sstr)<len(tstr): #could not matche
        return ""
    
    need=collections.Counter(tstr)
    missing=len(need) #missing is the unique character set length (hashmap length)
    minlen = len(sstr)+1 #add extra 1 to make at least one update (since we update only when size<minlen)
    minstart = -1
    start,end = 0,0
        
    while(end<len(sstr)):
        if sstr[end] in need:
            need[sstr[end]] -= 1
            if need[sstr[end]]==0:  #finished the match of current character
                missing-=1
        end += 1
        
        #when all unique characters in the hashmap (need) have been matched, loop to slide the lower window until the window size does not match all the hashmap of string2 anymore
        while(missing==0):  
            if sstr[start] in need: #if the window start character in the hashmap, add them back (as we are moving)
                need[sstr[start]] += 1
                if(need[sstr[start]] > 0):  #means now this character needs to be matched now
                    missing += 1
            #checking condition: if the current window size < minlen (update to find the minimum window)
            if(end-start<minlen): #if later ==minlen, not update (equal then choose the first one), only update less
                minstart=start
                minlen=end-start
            start+=1
    #use minstart to denote if ever matched once (if not, minstart remains -1)
    return sstr[minstart:minstart+minlen] if minstart>=0 else ""




## Another way(more concise): slightly different from the template
import collections
def minWindow(sstr, tstr):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    need=collections.Counter(tstr)  #contrsuct the hashmap of the string2 (to be matched)
    missing=len(tstr)
    minlen=len(sstr)
    minstart=minend=-1  
    start=end=0  #sliding window's two pointers
        
    while(end<len(sstr)): #loop through the string1 (used to match the other one)
        if(need[sstr[end]]>0): #if the current character in the hashmap, decrease the hashmap value -=1
            missing-=1
        need[sstr[end]]-=1
        end+=1 

        while(missing==0):
            if(need[sstr[start]]>=0):
                missing+=1
            need[sstr[start]]+=1
            if(end-start<=minlen):
                minstart=start
                minend=end
                minlen=end-start
            start+=1
        
    return sstr[minstart:minend]
        