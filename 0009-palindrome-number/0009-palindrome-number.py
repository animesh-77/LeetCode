class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)
        f, l= 0, len(x)-1
        while f<=l:
            if x[f] != x[l]:
                return False
            f+=1
            l-=1
        return True
        