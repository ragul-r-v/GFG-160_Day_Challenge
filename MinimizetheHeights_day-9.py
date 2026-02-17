class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()                          # Sort the array to make it easier to find the minimum and maximum heights after modification
        res = arr[n-1]-arr[0]               # Initialize the result as the difference between the maximum and minimum heights without any modification
        
        for i in range(1,len(arr)):         # Iterate through the sorted array starting from the second element
            if arr[i]-k<0:                  # If the current height minus k is negative, we cannot reduce it further, so we skip this iteration ,because we cannot have negative heights
                continue                    # Calculate the minimum and maximum heights after modification
            minH=min(arr[0]+k,arr[i]-k)     # The minimum height can be either the smallest height plus k or the current height minus k
            maxH=max(arr[i-1]+k,arr[n-1]-k) # The maximum height can be either the previous height plus k or the largest height minus k
            res=min(res,maxH-minH)          # Update the result with the minimum difference found so far
        return res                          # Return the minimum difference between the maximum and minimum heights after modification
if __name__ == "__main__":                  # Example usage
    arr = [1, 5, 8, 10]                     # The array of heights
    k = 2                                       # The value by which we can increase or decrease the heights
    ans = Solution().getMinDiff(arr, k)     # Calculate the minimum difference between the maximum and minimum heights after modification
    print(ans)                          # Print the result