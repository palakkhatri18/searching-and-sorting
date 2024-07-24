#User function Template for python3

# function should return a triplet
# if no such triplet is found return
# a container results as empty
def findTriplet(arr,n):
    # your code here
    arr.sort()
    result=[]
    
    for i in range(n):
        j, k = 0, i - 1
        while j<k:
            if arr[i]==arr[j]+arr[k]:
                result.append(arr[i])
                result.append(arr[j])
                result.append(arr[k])
                return result
            elif arr[i]>arr[j]+arr[k]:
                
                j=j+1
            else:
                k=k-1
    return result 