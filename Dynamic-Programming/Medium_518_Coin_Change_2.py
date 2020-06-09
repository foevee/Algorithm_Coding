"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
 

Note:
You can assume that
0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer


Method: Unbounded KnapPack
Knappack problem with unbounded capacity, use dp[i][m] denotes using the first i coins to make amount m
- initialize dp[i][0]=1 for later add
- at each dp[i][m] count if using the ith coin (index i-1)
  - first consider not using ith coin: then dp[i][m] = dp[i-1][m]
  - then consider using ith coin if only the ith coin amount <= m: then add more combs (from using ith coin with amount coins[i-1]),
    dp[i][m] += dp[i][m-coins[i-1]]
	(here we can see if m==coins[i-1], we should have dp[i][m]+=1, so we need to initialize all dp[i][0]=1)

Complexity: Time O(M*N) Space O(M*N)
"""

def change(self, amount: int, coins: List[int]) -> int:
    ncoins = len(coins)
    #dp[i][m] tracks the # of combinations using first i coins to make amount m
    dp = [[0]*(amount+1) for _ in range(ncoins+1)]
	dp[0][0] = 1
	
	for i in range(1, ncoins+1):
		dp[i][0] = 1 #initialize, just 1 # of combns to make amount 0
		for m in range(1, amount+1):
			#1) use only previous i-1 coins
			dp[i][m] = dp[i-1][m]
			if coins[i-1]<=m:
				#2) if the ith coin could be used, add the combs of using the ith coin
				#notice using dp[i][m-coins[i-1]] here rather than dp[i-1][..] since coins are infinite
				dp[i][m] += dp[i][m-coins[i-1]]
	
	return dp[ncoins][amount]