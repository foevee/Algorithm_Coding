"""
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
 
Constraints:
3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300

"""
#Optimal Solution: use a sorted hashset and iterate through sorted hashset key (fix first, then use two sum way to find next)
#notice we will discuss count rule for x+y+z==target by (1)x==y==z (2)x==y<z (2)x<y==z (4)x<y<z
from collections import Counter
def threeSumMulti(self, arr: List[int], target: int) -> int:
    arrCount = Counter(arr)
    nkey = len(arrCount)
    sorted_keys = sorted(arrCount) #we must use sorted key number to loop (thus can two pointer iteration (two num))
    MOD = 10**9+7
    count = 0
    for i, key in enumerate(sorted_keys):
        j, k = i, nkey-1 #notice j start from i since we can have x==y==key or key==x<y
        twoSumTarget = target-key
        #use two sum way (two pointers) to find the next two 
        while j<=k:
            x, y = sorted_keys[j], sorted_keys[k]
        
            if x+y<twoSumTarget:
                j += 1
            elif x+y>twoSumTarget:
                k -= 1
            else:
                if x==y==key: count += arrCount[key]*(arrCount[key]-1)*(arrCount[key]-2)//6 #if x==y==z, then C(count[x],3)
                elif key==x: count += arrCount[y]*arrCount[key]*(arrCount[key]-1)//2        #if x==y<z, then C(count[x],2)*count[z]
                elif x==y: count += arrCount[key]*arrCount[x]*(arrCount[x]-1)//2            #if x<y==z, then C(count[y],2)*count[x]
                else: count += arrCount[key]*arrCount[x]*arrCount[y]                        #if x<y<z, then count[x]*count[y]*count[z]
                j += 1
                k -= 1
                count %= MOD
                
    return count%MOD
