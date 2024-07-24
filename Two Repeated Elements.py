class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        s=set()
        l1=[]
        i=0
        for i in arr:
            if i in s:
                l1.append(i)
            else:
                s.add(i)
        return l1