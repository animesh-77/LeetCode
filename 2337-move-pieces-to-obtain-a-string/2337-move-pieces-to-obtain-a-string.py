class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        start_LRs= [(c, i) for i,c in enumerate(start) if c!= '_']
        target_LRs= [(c,i) for i,c in enumerate(target) if c!= '_']
        
        if len(start_LRs) != len(target_LRs):
            return False
        
        for start_c, target_c in zip(start_LRs, target_LRs):
            if start_c[0] != target_c[0]:
                # Check both L or R
                return False
            # Now both are L or both are R
            elif target_c[0] == "L":
                if start_c[1] < target_c[1]:
                    return False
                
            elif target_c[0] == "R":
                if start_c[1] > target_c[1]:
                    return False
        
        return True