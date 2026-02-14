class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        res = arr[n-1]-arr[0]
        
        for i in range(1,len(arr)):
            if arr[i]-k<0:
                continue
            minH=min(arr[0]+k,arr[i]-k)
            maxH=max(arr[i-1]+k,arr[n-1]-k)
            res=min(res,maxH-minH)
        return res
if __name__ == "__main__":
    arr = [1, 5, 8, 10]
    k = 2
    ans = Solution().getMinDiff(arr, k)
    print(ans)