class Solution:
    
    def get_primes(self):
        
        ret = []
        for num in range(2,1000):
            for factor in range(2, (num//2)+1):
                if num%factor == 0:
                    break
                    
            else:
                ret.append(num)
        return ret
                
            
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        all_primes= self.get_primes()
        # print(all_primes[:10])
        
        for pos in range(len(nums)-1, 0, -1):
            
            num= nums[pos]
            last_num= nums[pos-1]
            
            if num > last_num:
                continue
             
            # last_num > num
            for minus_num in all_primes:
                
                new_last_num = last_num- minus_num
                if new_last_num <= 0:
                    return False
                elif new_last_num < num:
                    # print("USING ", minus_num)
                    nums[pos-1]= new_last_num
                    print("NOW ",nums[pos-1], nums[pos])
                    break
            else:
                return False
        print(nums)           
        return True
                    
        