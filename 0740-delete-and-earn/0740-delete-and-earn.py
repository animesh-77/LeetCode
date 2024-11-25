class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        max_num= max(nums)
        sums_i = [0]*(max_num+1)
        
        for num in nums:
            sums_i[num] += num
            
        select_i, not_select_i = [0]*len(sums_i), [0]*len(sums_i)
        
        select_i[0]= sums_i[0]
        
        select_i[1]= sums_i[1]
        not_select_i[1]= max(select_i[0], not_select_i[0])
        
        for i in range(2, len(sums_i)):
            
            select_i[i]= not_select_i[i-1] + sums_i[i]
            not_select_i[i]= max(select_i[i-1], not_select_i[i-1])
            
        # print(select_i[-1], not_select_i[-1])
        return max(select_i[-1], not_select_i[-1])