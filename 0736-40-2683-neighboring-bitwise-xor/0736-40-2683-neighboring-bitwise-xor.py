class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        a= 0
        for num in derived:
            a ^= num

        return a == 0
        