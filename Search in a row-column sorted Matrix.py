class Solution:
    
    #Function to search a given number in row-column sorted matrix.
        def search(self,matrix, n, m, x): 
            # code here 
            low=0
            high=m-1
            while low < n and high>=0:
                
                if matrix[low][high]==x:
                    return 1
                elif matrix[low][high]>x:
                    high=high-1
                    #left
                else:
                    low=low+1 
                    #down
            return 0