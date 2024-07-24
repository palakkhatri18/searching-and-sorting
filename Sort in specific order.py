# Given an array A of positive integers. Your task is to sort them in such a way that the first part of the array contains odd numbers sorted in descending order, rest portion contains even numbers sorted in ascending order.
class Solution:
    def sortIt(self, arr, n):
        arr.sort()
        even = []
        odd = []
        for i in range(n):
            if arr[i]%2==0:
                even.append(arr[i])
            else:
                odd.append(arr[i])
        arr[::] = odd[::-1] + even 