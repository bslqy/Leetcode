class Solution(object):
    def fib(self, N):
        """
        DP
        :type N: int
        :rtype: int
        """
        #
        if N == 0:
            return 0
        if N == 1:
            return 1

        dp = {}
        dp[0] = 0
        dp[1] = 1

        for i in range(2,N+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[N]

if __name__ == '__main__':
    print(Solution().fib(4))