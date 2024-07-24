# Given two arrays of length N and M, print the merged array in ascending order containing only unique elements.

class Solution:
    def mergeNsort(self, a, b, n, m, answer):
        # Write your code here
        z=set(a+b)
        answer[:]=list(sorted(z))
        return len(z)