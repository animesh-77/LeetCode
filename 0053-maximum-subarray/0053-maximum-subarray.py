class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        lenNums= len(nums)
        
        
        maxTillNow= [0]* lenNums
        
        maxTillNow[0]= nums[0]
        maxSum= nums[0]
        
        for pos in range(1, lenNums):
            
            maxTillNow[pos]= max(maxTillNow[pos-1]+ nums[pos], nums[pos])
            maxSum= max(maxTillNow[pos], maxSum)
            
            
        return maxSum