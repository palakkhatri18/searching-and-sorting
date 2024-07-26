
class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot - 1)
            self.quickSort(arr, pivot + 1, high)
    
    def partition(self, arr, low, high):
        p = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] <= p:
                i = i + 1
            while i <= j and arr[j] >= p:
                j = j - 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        return j