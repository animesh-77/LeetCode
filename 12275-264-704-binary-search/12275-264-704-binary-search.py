class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import bisect

        i = bisect_left(nums, target)
        if i != len(nums) and nums[i] == target:
            return i
        return -1