# Given an array arr[ ] of N elements, your task is to find the minimum number of increment operations required to make all the elements of the array unique. ie- no value in the array should occur more than once. In an operation a value can be incremented by 1 only.
class Solution:
    def minIncrements(self, arr, N): 
        # Code here
        arr.sort()
        count = 0
        
        for i in range(1, N):
            if arr[i] <= arr[i - 1]:
                increment = arr[i - 1] - arr[i] + 1
                arr[i] += increment
                count += increment
        
        return count        
