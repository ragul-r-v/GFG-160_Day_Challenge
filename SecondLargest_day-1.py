class Solution:

    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return -1

        first = second = float('-inf')
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num

        if second == float('-inf'):
            return -1
        else:
            return second

# -------- Driver Code --------
if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    
    obj = Solution()
    result = obj.getSecondLargest(arr)
    
    print("Second Largest:", result)