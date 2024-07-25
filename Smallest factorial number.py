class Solution:
    
    def countTrailingZeroes(self, x):
        count = 0
        f = 5
        while x >= f:
            count += x // f
            f *= 5
        return count
    
    def findNum(self, n : int):
        if n == 0:
            return 0

        low, high = 0, 5 * n
        while low < high:
            mid = (low + high) // 2
            if self.countTrailingZeroes(mid) >= n:
                high = mid
            else:
                low = mid + 1
        return low