class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 动态规划

        l = len(s)
        longest = ""
        memo = [[False for i in range(l)] for j in range(l)]

        # len = 1
        for i in range(l):
            memo[i][i] = True
            longest = s[i:i+1]
        # len = 2
        for i in range(l - 1):
            if s[i] == s[i+1]:
                memo[i][i+1] = True
                if(len(s[i:i+2]) > len(longest)):
                    longest = s[i:i+2]

        # len > 2
        """
        Step from 2 to len(s)
        """
        for step in range (2,l+1):
            # 最多跳几次，再跳就越界
            for i in range(l- step ):
                j = i + step
                if s[i] == s[j] and memo[i+1][j-1]:
                    longest = s[i:j+1]

                    memo[i][j] = True

        return longest
if __name__ == '__main__':
    print(Solution().longestPalindrome('cbbd'))

