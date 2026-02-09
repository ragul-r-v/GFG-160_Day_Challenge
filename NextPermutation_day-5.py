class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        
        pivot = -1
        for i in range(n -2,-1, -1):
            if arr[i] < arr [i +1]:
                pivot = i
                break
        
        
        if pivot == -1:
            arr.reverse()
            return
        
        for i in range(n -1,pivot,-1):
            if arr[i] > arr[pivot]:
                arr[i],arr[pivot] = arr[pivot],arr[i]
                break
            
        left,right = pivot + 1,n-1
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -=1

## for vs code run  

if __name__ == "__main__":
    arr = [3, 2, 1]
    obj = Solution()
    obj.nextPermutation(arr)
    print(*arr)
            