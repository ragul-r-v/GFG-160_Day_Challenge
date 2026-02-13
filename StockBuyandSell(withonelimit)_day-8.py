class Solution:
    def maximumProfit(self, prices):
        minSoFar = prices[0]
        res = 0

        for i in range(1, len(prices)):
            minSoFar = min(minSoFar, prices[i])
            res = max(res, prices[i] - minSoFar)

        return res


if __name__ == "__main__":
    prices = [7,10,1,3,6,9,2]
    obj = Solution()
    print(obj.maximumProfit(prices))




class Solution:
    def maximumProfit(self, prices):
        minSoFar = prices[0]
        profit = 0

        for price in prices:
            minSoFar = min(minSoFar, price)
            profit = max(profit, price - minSoFar)

        return profit


if __name__ == "__main__":
    prices = [7,10,1,3,6,9,2]
    print(Solution().maximumProfit(prices))
