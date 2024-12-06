class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned= {i:None for i in banned}
        
        curSum, curNums= 0, 0
        
        for num in range(1, min(n, maxSum)+1):
            
            if num not in banned:
                
                if (curSum+ num) <= maxSum:
                    # print(num)
                    curSum += num
                    curNums += 1
                    
                else:
                    break
        
        return curNums
                    
                
        