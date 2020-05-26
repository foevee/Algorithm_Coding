"""
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

 

Example 1:
Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]

Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.
 

Note:
Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.


Method: Use a stack (LIFO) to save each (price, span) pair
Whenever a new price comes in, we will start to count its span, loop through all the stack to find all previous max continuous span
  The loop runs continuously only when each stack item has price <= current price and stack is non-empty 
  (once not satisfied, the loop breaks, thus making sure only pop out the <= price in the stack)
  in the loop, we pop out the stack item (stack[-1]) and add this item's span to the curr_span
  notice we will only pop out the item of those <= curr_price, and include its span into curr_span
outside the loop, push back the current (price,  curr_span) pair to the stack

In this way, the new pushed pair actually include all its previous poped out price's span (those price<=curr_price), 
  and thus count a sequence of non-decreasing prices into one price and the span (the sequence length).
Notice when poping out the item (price0, span0), this price will not be omitted during later price's (price2) count, 
  instead it will be counted in the current price's (price1) span and can still be counted later. 
  For example: if price2>price1, then price2 will count price1's span. Since price0 pair was poped during price1's span count, so  
    price1's span includes price0's span, and thus price2 include considering the price0.

Each new price only tracks those price <= current price, and add back the span into the stack, 
in this way to save space of looping through all element and avoiding "Time Limit Error"

Since each price (item) will only be poped out once and pushed in once, so 2 * N times stack operations and N times calls
Complexity: Time - worst O(N), amortized O(1), Space - O(N)

"""



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class StockSpanner:
    def __init__(self):
        self.stack = []  #save each pair of (price, span)
        
    def next(self, price: int) -> int:
        curr_span = 1 #at least include itself
        
        #only pop those <= price (thus will reflect in this price's span)
        #once not <=, break the loop and thus get only consecutive max span
        while(self.stack and self.stack[-1][0]<price):
            #only loop to pop when previous price <= price in case pop the non-less one (need eveluate first before pop)
            _, s = self.stack.pop()
            curr_span += s #when previous price <= price
        
        self.stack.append((price, curr_span)) #add today's price into stack
        return curr_span
        


