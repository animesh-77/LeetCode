class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 ==1:
            return False
        brackets_map= {")":"(",
               "]":"[",
               "}": "{"}
        
        brackets= []
        for c in s:
            if c in "([{":
                brackets.append(c)
            else:
                try:
                    if brackets and brackets_map[c] != brackets[-1]:
                        return False
                    else:
                        brackets.pop(-1)
                except:
                    return False
        else:
            if len(brackets)==0:
                return True
            else:
                return False