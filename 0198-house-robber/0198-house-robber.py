class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob_num_prev, not_rob_num_prev= 0, 0
        
        for num in nums:
            
            not_rob_num = max(rob_num_prev, not_rob_num_prev)
            rob_num= not_rob_num_prev+ num
            
            rob_num_prev, not_rob_num_prev= rob_num, not_rob_num
            
        return max(not_rob_num, rob_num)
            
        
        
        