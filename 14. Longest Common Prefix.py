class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        current = d[s[0]]
        ans = current
        for i in range(1,len(s)):
            if d[s[i]] < current:
                ans = ans - d[s[i]]
                current = d[s[i]]
            elif d[s[i]] >= current:
                ans = ans + d[s[i]]
                current = d[s[i]]

        return ans




if __name__ == '__main__':
    print(Solution().romanToInt("III"))