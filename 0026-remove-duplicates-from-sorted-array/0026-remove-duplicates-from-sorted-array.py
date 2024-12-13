class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        unqiueNums= [nums[0]]
        k= 1
        
        for num in nums[1:]:
            if num != unqiueNums[-1]:
                unqiueNums.append(num)
                k += 1
        
                
        for i, unqiueNum in enumerate(unqiueNums):
            nums[i]= unqiueNum
            
        
        return k
        
        
        