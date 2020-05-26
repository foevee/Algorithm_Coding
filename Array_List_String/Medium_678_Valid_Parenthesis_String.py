"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "(*)"  Output: True
Example 2:
Input: "(**)))" Output: True

Note: The string size will be in the range [1, 100].


Solution:
Brute Force:
Loop through each *, treat them as 3 ways and see if the string is matched
Complexity: O(N*3^k) time (k is the # of *), O(1) space

Optimal Way:
Use two count to track the maximum and minimum potential required num of the right parenthesis ')'
since * can choose to be ['(',empty,')'], we need to find the range of required ')' for match
We count the required num of ')' by +1 for '(' and -1 for ')' (so if more '(' then ')', we need positive num of ')')
    If '(', both count +=1;  If ')', both count -= 1; if '*', count_max+=1, count_min-=1

Two checking criteria:
(1) If the maximum required num is even < 0, means too many ')', even treat all '*' as '(' has no help  => False
    we need to check (1) at each iteration since  ')' cannot appear before '(' (after excluding matched '()' pair)
(2) If the minimum requred num is even >0, means too many '(', even treat all '*' as ')' has no help  => False

Three potential results:
(a) '(' total num more than ')', use (2) to return False
(b) ')' total num more than '(' or ')' appear before '(' at certain time, use (1) to return False
(c) '(' and )' are matched, there must have count_max>=0, count_min=0

!! Notcie we set count_min will never be negative (otherwise no point for tracking the minimum required), 
    but it won't betray the checking constraint, since when too many ')' and count_min<0, then count_max must < 0, so we can use (1) constraint to find out.

Complexity: O(N) time, O(1) space
"""
def checkValidString(self, string: str) -> bool:
    count_max, count_min = 0, 0
    for s in string:
        if s=='(':
            count_max += 1
            count_min += 1
        elif s==')':
            count_max -= 1
            count_min -= 1
        else: # s==*
            count_max += 1 #treat # as '('
            count_min -= 1 #treat # as ')'

        if count_min<0:  #count_min will never be less then 0, otherwise make no point (the least required ')' num should be non-negative)
            count_min = 0
        # at each iteration, we check if count_max<0, which means too many ')', even treat all * as '(' still can not help, so return False
        if(count_max<0):
            return False
        
        return count_min==0