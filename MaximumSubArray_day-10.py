class Solution:                 # Define a class named Solution
    def maxSubarraySum(self, arr):  # Define a method named maxSubarraySum that takes an array as input
        res = arr[0]                   # Initialize the result as the first element of the array, which is the maximum sum of a subarray found so far
        maxEnding = arr[0]          # Initialize maxEnding as the first element of the array, which is the maximum sum of a subarray that ends at the current index
        
        for i in range(1,len(arr)):     # Iterate through the array starting from the second element
            
            maxEnding = max(maxEnding + arr[i],arr[i])      # Update maxEnding by comparing the sum of the current maxEnding and the current element with the current element itself. This step decides whether to extend the existing subarray or start a new subarray at the current index.
            res = max(res,maxEnding)                    # Update the result by comparing the current result with maxEnding. This step keeps track of the maximum sum of any subarray found so far.
            
        return res                                      # Return the maximum sum of a subarray found in the array
    
if __name__ == "__main__":                              # Example usage
    arr = [-2,1,-3,4,-1,2,1,-5,4]                       # The input array for which we want to find the maximum sum of a subarray
    ans = Solution().maxSubarraySum(arr)                # Calculate the maximum sum of a subarray in the input array
    print(ans)                                          # Print the result, which is the maximum sum of a subarray in the input array