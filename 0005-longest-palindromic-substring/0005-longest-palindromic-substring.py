class Solution:
    
    # def isPalindromeFirstLast(self, s:str) -> str:
        
    def longestPalindrome(self, s: str) -> str:
        
        is_pal = [[False] * len(s) for _ in range(len(s))]
        
        max_pal_str= s[0]
        
        for row in range(len(s)):
            is_pal[row][row]= True
            
            if row < len(s)-1:
                    
                    if s[row]==s[row+1]:
                        is_pal[row][row+1]= True
                    
                        new_pal = s[row:row+2]
                        if len(new_pal) > len(max_pal_str):
                            max_pal_str= new_pal
            
        
        for row in range(len(s)-3,-1,-1):
            for col in range(row+2, len(s)):
                if s[row] == s[col] and is_pal[row+1][col-1] is True:
                    is_pal[row][col] = True
                    
                    new_pal= s[row:col+1]
                    if len(new_pal) > len(max_pal_str):
                        max_pal_str= new_pal
                    
                    
        # for row in range(len(s)):
        #     print(is_pal[row])
        
        return max_pal_str   
        