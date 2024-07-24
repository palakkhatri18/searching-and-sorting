class Solution:
    def select(self, arr, i):
        # This method selects the minimum element starting from index i
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index
    
    def selectionSort(self, arr, n):
        # Perform selection sort
        for i in range(n - 1):
            # Find the minimum element in the unsorted part of the array
            min_index = self.select(arr, i)
            
            # Swap the found minimum element with the first element of the unsorted part
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]