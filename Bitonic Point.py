class Solution:

	def findMaximum(self,arr, n):
		# code here
		arr.sort()
		
		return arr[-1]