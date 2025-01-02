class Solution:
    from random import randint

    def sortArray(self, nums: List[int]) -> List[int]:

        def quickSort(left, right):

            if left >= right:
                return

            pivotNum = nums[randint(left, right)]

            current, lessThanPointer, moreThanPointer = left, left - 1, right + 1

            while current < moreThanPointer:
                # print(
                #     f"{current=} {nums[current]=} {lessThanPointer=} {moreThanPointer=}"
                # )
                if nums[current] < pivotNum:
                    lessThanPointer += 1
                    nums[current], nums[lessThanPointer] = (
                        nums[lessThanPointer],
                        nums[current],
                    )
                    current += 1
                elif nums[current] > pivotNum:
                    moreThanPointer -= 1
                    nums[current], nums[moreThanPointer] = (
                        nums[moreThanPointer],
                        nums[current],
                    )
                else:
                    current += 1

            quickSort(left, lessThanPointer)

            quickSort(moreThanPointer, right)

        quickSort(0, len(nums) - 1)
        print(nums)
        return nums
