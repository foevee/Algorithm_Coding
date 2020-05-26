"""
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.


Solution:
use each sorted word string as key to save them into a dictionary
    since all words in the same group will have the same sorted word (denoted in string)
return the dictionary values, which is a list
"""


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    count = {}
    for num in strs:
        key = "".join(sorted(num))
        count[key] = count.get(key,[]) + [num]  #add in num to its related list
    return count.values()