class Solution:
    def sortedMerge(self, a, b, c, n, m):
        # Your code goes her
        x=a+b
        for i in range(n+m):
            c[i]+=x[i]
        c.sort()
        return c