class Solution:
    
            
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        import math
        import bisect

        def checkValid(Pen: int)-> bool:
        
            ops= 0
            for num in nums:

                ops += int(math.ceil((num- Pen)/Pen))

                if ops > maxOperations:
                    break

            return ops <= maxOperations
    
    
        
        minPen, maxPen= 1, max(nums)
        
        
        optPen= bisect.bisect_left(range(1, max(nums)), True, key=checkValid) + 1
            
        return optPen
            
        