def maxProduct(arr):    # Function to find the maximum product subarray
    n = len(arr)        # Length of the input array
    currMax = arr[0]        # Initialize current maximum product to the first element of the array
    currMin = arr[0]        # Initialize current minimum product to the first element of the array
    maxProd = arr[0]        # Iterate through the array starting from the second element

    for i in range(1, n):       # Calculate the temporary maximum product by considering the current element, the product of the current element with the current maximum, and the product of the current element with the current minimum
        temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)      # Calculate the temporary minimum product by considering the current element, the product of the current element with the current maximum, and the product of the current element with the current minimum
        currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)   # Update the current maximum product to the temporary maximum product
        currMax = temp                                              # Update the overall maximum product if the current maximum product is greater than the overall maximum product
        maxProd = max(maxProd, currMax)                             # Return the overall maximum product
    return maxProd                                                  # Example usage

if __name__ == "__main__":      # Define an example input array and print the result of the maxProduct function
    arr = [-2,6,-3,-10,0,2]     #   Input array for testing
    print(maxProduct(arr))      # Output the maximum product of a subarray in the input array