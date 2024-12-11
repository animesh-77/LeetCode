class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lenPrices= len(prices)
        
        LowestTillNow= [0]* lenPrices
        LowestTillNow[0]= prices[0]
        
        
        sellToday= [0]* lenPrices
        
        maxProfit= 0
        
        for pos in range(1, lenPrices):
            sellToday= prices[pos]- LowestTillNow[pos-1] 
            LowestTillNow[pos]= min(LowestTillNow[pos-1], prices[pos])
            
            maxProfit= max(sellToday, maxProfit)
            
            
        return maxProfit