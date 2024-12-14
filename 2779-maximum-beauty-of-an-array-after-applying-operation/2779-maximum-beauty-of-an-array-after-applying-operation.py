class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        lenNums= len(nums)
        i,j= 0, 0
        maxLen= 0
        
        while i< lenNums and j< lenNums:
            left, right= nums[i], nums[j]
            if right- left <= 2*k:
                maxLen= max(j-i+1, maxLen)
                j += 1
                
            if right- left > 2*k:
                i += 1
                
        return maxLen
                
                
                
        