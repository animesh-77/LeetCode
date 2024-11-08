class Solution:
    
    # def get_pos_bits(self, num: int, 
    #                  pos_bits_count:dict, 
    #                  max_count: int) -> dict:
        
        
    
    
    def largestCombination(self, candidates: List[int]) -> int:
        
        max_count= 1
        pos = 0
        while True:
            count= 0
            all_zeros= True
            
            for idx in range(len(candidates)):
            
                num = candidates[idx]
                last_bit = num- ((num>>1)<<1)
                if last_bit == 1:
                    count += 1
                
                candidates[idx] = candidates[idx]>>1
                if candidates[idx] > 0:
                    all_zeros = False
                    
                
            else:
                # print(pos, count)
                # print(candidates)
                if max_count< count:
                    max_count = count
                    
            if max_count == len(candidates):
                break 
            if all_zeros:
                break
                
            pos += 1
                
        return max_count
            
        