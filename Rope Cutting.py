class Solution:
    def RopeCutting (self, arr, n) : 
        #Complete the function\
        arr.sort()
        arr2=[]
        current=arr[0]
        j=0
        while current != arr[n-1]:
            if arr[j]-current>0:
                arr2.append(n-j)
                current=arr[j]
            j=j+1
        return arr2