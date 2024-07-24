class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        found = False
        arr.sort()
        for i in range(n - 1):
            l = i + 1
            r = n - 1
            x = arr[i]
            while l < r:
                if x + arr[l] + arr[r] == 0:
                    l += 1
                    r -= 1
                    found = True
                    break
                elif x + arr[l] + arr[r] < 0:
                    l += 1
                else:
                    r -= 1
            if found:
                break
        return found