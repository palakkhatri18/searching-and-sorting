class Solution:
    def countZeroes(self, A, N):
        count=0
        for i in range(N):
            for j in range(N):
                if A[i][j]==0:
                    count=count+1
        return count    