class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        import bisect
        import math
        
        def countPiles(candVal:int) -> bool:
            # print(f"{candVal=}")
            totalPiles= 0 # total piles of value candVal
            for candy in candies:
                L= int(math.ceil((candy- candVal)/ candVal))
                totalPiles += L
                totalPiles += 1 if (candy- L*candVal) == candVal else 0
                # print(f"{candy=} {totalPiles=}")
                if totalPiles >= k:
                    break
                
            return not(totalPiles >= k)        
        
        def sumMaxMin():
            totalCandies= 0
            minCandies, maxCandies= 1, candies[0]
            
            for candy in candies:
                totalCandies += candy
                maxCandies = max(maxCandies, candy)
                
            return minCandies, maxCandies, totalCandies
        
        minCandies, maxCandies, totalCandies= sumMaxMin()
        
        if totalCandies < k:
            return 0
        
        optCandy= bisect.bisect_right(range(minCandies, maxCandies+1), False, key= countPiles)

        return optCandy
        
        