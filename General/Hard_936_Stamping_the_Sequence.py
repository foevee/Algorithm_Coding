"""
You want to form a target string of lowercase letters.
At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.


Example 1:
Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)

Example 2:
Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]

Note:
1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.
"""

#Method: reverse match + greedy 
    #reversely match stamp or its covered version (first check whole stamp, if not then its covered version)
    #greedy search stamp in target string and replace each round matched stamp with *
    #we reversely iterate to see if each * covered stamp cover could ultimately replace target to all *
    #if it is (stamp possible), then each cover's first index reverse is the answer, otherwise return empty
def movesToStamp(self, stamp: str, target: str) -> List[int]:
    totalmatch = 0
    m, n = len(stamp), len(target)
    ans = []
    
    #outer loop keep iterating, might match smaller coveredstamp then back to larger coveredstamp iteratively
    while totalmatch<n:
        roundmatch = 0 #track each round match
        #revserly search matching size from m (whole) to 1 (can not be 0)
        for size in range(m, 0,-1): 
            for i in range(0,m-size+1):
                #we get the covered stamp (not substr of stamp) and find in target
                coveredstamp = '*'*i+stamp[i:i+size]+'*'*(m-size-i)
                pos = target.find(coveredstamp)
                #keep finding current matched coveredstamp in updated target, might have more than once
                while pos!=-1:
                    #update target
                    target = target[:pos] + '*'*m + target[pos+m:]
                    ans.append(pos)
                    roundmatch += size
                    pos = target.find(coveredstamp)
        
        #full round no match, early exit (in case dead look)
        if roundmatch==0: return []       
        totalmatch += roundmatch
                    
    return ans[::-1] #reversely matching need reverse
