class Solution:
    def merge(self,arr, l, m, r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        
        i = 0  # Initial index of the first subarray
        j = 0  # Initial index of the second subarray
        k = l  # Initial index of the merged subarray
        
        # Merge the temp arrays back into arr[l..r]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy the remaining elements of left[], if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # Copy the remaining elements of right[], if any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2  # Find the middle point
            self.mergeSort(arr, l, m)  # Sort first half
            self.mergeSort(arr, m + 1, r)  # Sort second half
            self.merge(arr, l, m, r)  # Merge the sorted halves