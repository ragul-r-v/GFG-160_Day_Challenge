

class Solution:
    def rotateArr(Self,arr,d):
        n = len(arr)
        d%=n
        reverse(arr, 0, d-1)
        reverse(arr, d, n-1)            
        reverse(arr, 0, n-1)

def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1

## for vs code run


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    d = 2
    obj = Solution()
    obj.rotateArr(arr,d)    
    print(*arr)
    