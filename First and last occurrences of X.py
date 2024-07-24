class Solution: 
    def firstAndLast(self, arr, n, x): 
        # Code here
        first = -1
        last = -1
        
        for i in range(n):
            if arr[i] == x:
                if first == -1:
                    first = i
                last = i
        
        if first == -1:
            return [-1]
        return [first, last] 