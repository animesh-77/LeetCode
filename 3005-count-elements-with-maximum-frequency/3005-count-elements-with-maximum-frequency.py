class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        all_nums= {}
        
        max_count= 0
        max_count_nums= {}
        
        for num in nums:
            
            all_nums[num]= all_nums.get(num, 0)+1
            
#             if all_nums[num] >= max_count:
#                 max_count= all_nums[num]
                
#                 max_count_nums[num]= max_count_nums.get(num, 0)+ 1
        
        
        max_count= max([all_nums[num] for num in nums])
        # print(all_nums)
        # print(max_count)
        total_max_count= 0
        
        for num in nums:
            if all_nums[num] == max_count:
                total_max_count += 1
                # print(total_max_count, num)
                

        return total_max_count
                