class Solution:
    
    # def isPalindromeFirstLast(self, s:str) -> str:
        
    def longestPalindrome(self, s: str) -> str:
        
        max_pal_str= ""
        
        for pos in range(len(s)):
            
            # odd length palindromes
            for offset in range(1,len(s)):
                left, right= pos-offset, pos+offset
                if left >= 0 and right < len(s):
                    if s[left]== s[right]:
                        new_pal = s[left:right+1]
                        if len(max_pal_str) < len(new_pal):
                            max_pal_str = new_pal
                    else:
                        break
                        
            # even length palindromes
            centre= pos+0.5
            for offset in range(0,len(s)):
                left, right= int(pos-offset-0.5), int(pos+offset+0.5)
                if left >= 0 and right < len(s):
                    if s[left]== s[right]:
                        new_pal = s[left:right+1]
                        if len(max_pal_str) < len(new_pal):
                            max_pal_str = new_pal
                            
                    else:
                        break
            
        return max_pal_str
                        
        