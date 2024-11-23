class Solution:
    import numpy as np
    
    
    def split_by_fixed(self, one_col: List[str]) -> List[List[str]]:
        
        from functools import reduce
        
        
        def split_logic(acc, x):
            if x == "*":

                # Start a new sublist if the split value is found
                acc.append([])  
            else:

                # Add the current value to the last sublist
                acc[-1].append(x)  
            return acc
        
        result = reduce(split_logic, one_col, [[]])
        return result
    
    
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        m_row, n_col= len(box), len(box[0])
        
        for row in range(m_row):
            # for col in range(n_col):

            one_row= box[row]
            all_sec= self.split_by_fixed(one_row)
            one_row= []
            
            for one_sec in all_sec:
                one_sec.sort(reverse= True)
                # print(one_sec)
                
                
                for item in one_sec:
                    one_row.append(item)
                one_row.append("*")
            # print(one_row)
            box[row]= one_row[:-1]
                
        import numpy as np
        
        rot_box= np.array(box)
        rot_box= rot_box[::-1,:].T
        
        
        return rot_box.tolist()
        