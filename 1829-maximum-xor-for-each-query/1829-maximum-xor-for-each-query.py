class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        
        full_num = 2**(maximumBit) - 1
        # print(full_num)
        ret= []
        
        A= nums[0]
        
        k = (A^full_num) & full_num
        ret.append(k)
        # print(A, ret[-1])
        
        for num in nums[1:]:
            
            A = A ^ num
            k = (A^full_num) & full_num
            ret.append(k)
            # print(A, ret[-1])
            
        return ret[::-1]