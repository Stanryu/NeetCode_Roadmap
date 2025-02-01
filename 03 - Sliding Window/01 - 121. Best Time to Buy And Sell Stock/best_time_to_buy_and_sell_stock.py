from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       left, right = 0, 1
       max_profit = 0

       while right < len(prices):
            if prices[left] >= prices[right]:
               left = right
            else:
               max_profit = max(max_profit, prices[right] - prices[left] )
            right += 1
           
       return max_profit

if __name__=='__main__':
    s = Solution()
    prices = [1,18,15,13,15,1,4,13]
    print(s.maxProfit(prices))