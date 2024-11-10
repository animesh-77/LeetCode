class Solution:
    def countBits(self, num: int) -> List[int]:
        
        ret= []
        
        for n in range(num+1):
            count = 0

            while n > 0:
                count +=1

                n= n&(n-1)

            ret.append(count)
            
        return ret