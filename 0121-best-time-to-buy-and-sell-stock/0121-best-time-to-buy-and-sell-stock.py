class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        max_profit = 0
        profit = 0

        for i in range(1, len (prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
            
            max_profit = max(profit, max_profit)
            
        return max_profit


       


        #   With TC - O(N)

        # min_till_now = prices[0]
        # profit = 0

        # for i in range(1,len(prices)):
        #     min_till_now = min(min_till_now, prices[i])

        #     profit = max(profit , prices[i] - min_till_now)

        # return profit

    
        # Time Complexity - O(N*N)
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):

        #         profit = prices[j] - prices[i]
        #         max_profit = max(profit,max_profit)

        # return max_profit




                

