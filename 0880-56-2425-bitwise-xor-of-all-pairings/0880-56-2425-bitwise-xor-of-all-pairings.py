class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        a= 0

        if len(nums2)&1 == 1:
            for num in nums1:
                a ^= num

        if len(nums1)&1 == 1:
            for num in nums2:
                a ^= num

        return a