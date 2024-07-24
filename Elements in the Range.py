# Elements in the Range
class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        ano = range(A , B+1)
        for i in ano:
            if i in arr:
                continue
            else:
                return False
        return True