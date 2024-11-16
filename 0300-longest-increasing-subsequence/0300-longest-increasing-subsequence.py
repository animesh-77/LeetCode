class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import numpy as np
        nums= np.array(nums)
        
        max_from_here= np.ones(len(nums))
        
        for pos in range(len(nums)-2, -1, -1):
            
            
            rem_arr= (1+ max_from_here[pos+1:])* (nums[pos] < nums[pos+1:])
            # print("Current ",nums[pos], "Rem array ",nums[pos+1:])
            # print("Current ",nums[pos], "Rem array ",rem_arr)
            
            max_from_here[pos]= max(1, rem_arr.max())
            # print("Current ",nums[pos], "Rem array ",max_from_here[pos+1:])
            
        # print(max_from_here)
        
        return int(max_from_here.max())
                
        