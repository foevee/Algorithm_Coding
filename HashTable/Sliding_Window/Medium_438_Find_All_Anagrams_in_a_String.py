"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Method: (Sliding window with result checking using "if window size == checking string length")
Construct a sliding window of two points start, end, name the checking string p as string2, the finding string s as string1

a.The general logic: use a [start, end] two pointers to denote a window
  for each fixed start, keep moving end pointer +1 till the current window could match the string2
  once the window get matched, move the start pointer +1 as a new start, and then move end to find a new window given this new start

b.Specific Step:
First use a hash map to save the hashtable of string2, use a counter variable to track the number of characters need to be matched
  set counter = len(hashmap)
Loop through the string1, at each step check the character in string2's hashtable
  if this character appeared, decreased the hashtable corresponding key-value -1
    check if the value of this character in the hashmap is 0, if it is, set counter -= 1, means we now finished matching of one character
    notice that we might have decreased the hashmap value to <=0 (since we have this character more than require), 
      but the counter will only be decreased once when the hashmap value == 0
    once finshed this hashmap checking, move end += 1
  at each round, check if the counter == 0  (means now the window could match the whold string2, but might be larger than required)
    if it is, we will keep doing the following until the counter is not 0 (thus using a loop)we
      we check if the current window has the desired length of string2, if yes then the current window is an anagram -- add them to result
      also, we will start to move the lower window higher (start+1) to find new matching window
        once if start+1, the current window does not include string1[start(before +1)] (set as c) anymore
        so we shall check if this character c is in hashtable, if it is, we need to add c back to hashtable, hashtable[c]+=1
        and if now the hashtable[c]>0, meaning we need to further match now, then we need to add counter += 1

Doing the above two procedures (one about end matching and moving, one about start matching and moving) until finishing looping string1

Complexity: O(N+K), Space: O(K) (K is the size of hashmap)

"""


import collections
def findAnagrams(self, string: str, p: str) -> List[int]:
    ## Use a sliding window to solve the problem
    result = []
    if len(string)<len(p):
        return result 
    count_dict = collections.Counter(p)
    start, end = 0,0
    counter = len(count_dict)  #denote how many characters in p remained to be matched
    for s in string:
        if s in count_dict:
            count_dict[s] -= 1
            if count_dict[s]==0:  #means this character is all matched
                counter -= 1
        #putting end+1 here instead of this round for loop's end, we can use end-start==len(p) rather than end-start+1==len(p)
        end += 1  
        while(counter==0):  #once the current window (start->end) find all matched, slide the lower window start+1
            s_ = string[start]
            if s_ in count_dict:
                count_dict[s_] += 1 #add back previous decreased (since windows sliding)
                if (count_dict[s_]>0):  #if this character is counted >0, counter += 1 (need match now)
                    counter += 1
            #check if the last matched window is anagram (since word could match, just need checking length)
            if end-start==len(p):
                result.append(start)
            start += 1
        
    return result