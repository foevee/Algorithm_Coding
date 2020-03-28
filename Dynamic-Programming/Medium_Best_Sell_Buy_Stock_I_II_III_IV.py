"""
Maximum Profit: Best Time to Buy and Sell Stock I(121), II(), III, IV
    type prices: List[int]
    rtype: int
"""

#Problem I: Only buy and sell at most 1 time
def maxProfit_I(prices):
    #Loop one time, save the minimum price upon now, calculate the maximum profit
    minp,profit=float('inf'),0
    for i in range(len(prices)):
        minp=min(minp,prices[i])
        profit=max(profit,prices[i]-minp)
    return profit

#Problem: Buy and Sell many times, but buy one sell one, no multiple buys or sells
def maxProfit_II(self, prices):
    #Sum all the increasing gap (each low peak buy, each high peak sell)
    profit=0
    for i in range(1,len(prices)):
        #if incresing, can add up
        #the same as buy in the lowest peak and sell at the highest peak
        profit+=max(prices[i]-prices[i-1],0)
    return profit
            
        

if __name__ == "__main__":
    Prices=[7,6,4,3,1]
    profit=maxProfit_I(Prices)
    #profit=maxProfit_II(Prices)
    print(profit)
