class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(n):
            # Last i elements are already sorted
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    # Swap if the element found is greater than the next element
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]