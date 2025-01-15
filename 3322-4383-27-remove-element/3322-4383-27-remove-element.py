class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums== []:
            return len(nums)
        otherNums= [] if nums[0]== val else [nums[0]]
        
        for num in nums[1:]:
            # print(f"{num=}")
            if num != val:
                otherNums.append(num)
                # print(f"{otherNums=} {val=}")

        for i, num in enumerate(otherNums):
            nums[i]= num

        return len(otherNums)
