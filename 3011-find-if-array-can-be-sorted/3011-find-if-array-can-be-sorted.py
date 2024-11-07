class Solution:
    def set_bits(self, num) -> int:
        count = 0
        while num:
            num &= num - 1
            count += 1
        return count

    def canSortArray(self, nums: List[int]) -> bool:
        
        bit_count= {}
        for num in nums:
            if num not in bit_count:
                bit_count[num]= self.set_bits(num)
        
        
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j+1] < nums[j]:
                    # we need to swap
                    if bit_count[nums[j+1]] != bit_count[nums[j]]:
                        return False
                    
                    a= nums[j+1]
                    nums[j+1]= nums[j]
                    nums[j]= a
        
        return True
        