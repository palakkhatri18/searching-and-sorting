# Given an array A of integers and another number K. Find all the unique quadruple from the given array that sums up to K.

# Also note that all the quadruples which you return should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.

class Solution:
    def fourSum(self, arr, k):
        n = len(arr)
        arr.sort()
        quadruples = set()

        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    sum = arr[i] + arr[j] + arr[left] + arr[right]
                    if sum == k:
                        quadruples.add((arr[i], arr[j], arr[left], arr[right]))
                        left += 1
                        right -= 1
                        while left < right and arr[left] == arr[left - 1]:
                            left += 1
                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1
                    elif sum < k:
                        left += 1
                    else:
                        right -= 1

        result = [list(quad) for quad in sorted(quadruples)]
        return result