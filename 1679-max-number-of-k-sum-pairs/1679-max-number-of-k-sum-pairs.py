class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        left, right= 0, len(nums)-1
        count=0
        
        while left<= right:
            
            # print(f"{left=} {right=}")
            if nums[left]+ nums[right]== k and left!= right:
                
                left+= 1
                right-= 1
                count+= 1
                
            elif nums[left]+ nums[right] > k:
                right -= 1
                
            elif nums[left]+ nums[right] < k:
                left+= 1
                
            elif left== right:
                break
                
        return count
        