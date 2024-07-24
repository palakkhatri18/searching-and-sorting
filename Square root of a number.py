class Solution:
    def floorSqrt(self, x):
        import math
        sqrt_value = math.sqrt(x)  # Calculate the square root of x
        return math.floor(sqrt_value)  # Return the floor value of the square root
    
    
    # without importing math
    # class Solution:
    # def floorSqrt(self, x):
    #     a = int(x**0.5)
    #     if a:
    #         return a