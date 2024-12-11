class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        lenPrices= len(nums)
        
        LowestTillNow= [0]* lenPrices
        LowestTillNow[0]= nums[0]
        
        
        sellToday= [0]* lenPrices
        
        maxProfit= 0
        
        for pos in range(1, lenPrices):
            sellToday= nums[pos]- LowestTillNow[pos-1] 
            LowestTillNow[pos]= min(LowestTillNow[pos-1], nums[pos])
            
            maxProfit= sellToday if pos==1 else max(sellToday, maxProfit)
            
            # if maxProfit == sellToday:
            #     print(f"{nums[pos]=} {LowestTillNow[pos]=} {maxProfit}")
            
            
        return maxProfit if maxProfit>0 else -1
        