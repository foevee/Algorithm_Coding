"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:
"cccaaa"
Output:
"cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:
"Aabb"
Output:
"bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Method:
The key is to use a hashmap to save the count of each character and then re-organize the string according to the count of each chracter
1. One way (using sort): sort the hashmap (dict) based on value descendingly, and then add the key*value ('a'*3 means 'aaa') one by one
2. Another way: save the hashmap into a list, use index as value, list value as key (character), then we loop the list and add each value (substring), then return its reverse string which is indeed the characters sorted by the count descendingly


"""

#One way: using sort
import collections
def frequencySort(s: str) -> str:
    count = collections.Counter(s)
    sort_count = sorted(count.items(), key=lambda item: (-item[1], item[0]))
    res = ""
    for k,v in sort_count:
        res += k*v
    return res


#Another way: not using sort
def frequencySort(self, s: str) -> str:
    count = collections.Counter(s)
    freq_list = ['' for i in range(len(s)+1)]
    for k,v in count.items():
        freq_list[v]+=k*v
    res = ""
    for item in freq_list:
        res+=item
    return res[::-1]