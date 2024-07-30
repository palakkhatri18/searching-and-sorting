
class Solution:
        
        #Function to find the minimum number of swaps required to sort the array.
        def minSwaps(self, nums):
            #Code here..........
            n = len(nums)
            temp = nums.copy()
            temp.sort()
            track = dict()
            
            for i in range(n):
                track[nums[i]] = i
                swap = 0
                
            for i in range(n):
                if nums[i] != temp[i]:
                    swap += 1
                    a, b = nums[i], temp[i]
                    nums[i], nums[track[b]] = nums[track[b]], nums[i]
                    track[a], track[b] = track[b], track[a]       
            return swap