class Solution:
    
    def get_pos_bits(self, num: int, pos_bits_count:dict) -> dict:
        
        pos = 0
        while num > 0:
            last_bit= num- ((num>>1)<<1)
            if last_bit == 1:
                pos_bits_count[pos] = pos_bits_count.get(pos, 0) + 1
                
            num = num>>1
            pos += 1
            
        return pos_bits_count
    
    
    def largestCombination(self, candidates: List[int]) -> int:
        
        pos_bits_count= {}
        for num in candidates:
            pos_bits_count = self.get_pos_bits(num, pos_bits_count)
            # print(num, pos_bits_count)
            
        max_count= 1
        for pos, count in pos_bits_count.items():
            if count > max_count:
                max_count = count
                
        return max_count
            
            
        