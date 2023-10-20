class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for start in range(len(haystack)):
            check_str= haystack[start: start+len(needle)]
            
            if check_str == needle:
                return start
            
        return -1
        