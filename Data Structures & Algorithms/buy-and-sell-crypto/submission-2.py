class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i,x in enumerate(prices):
            for j in range(i+1,len(prices)):
                #range不包括最右边，包括最左边
                n = prices[j]
                ans = max(ans, n - x)
        return ans