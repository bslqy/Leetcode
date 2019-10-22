class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            a = int(str(x)[::-1])
        if x <= 0:
            a = -1*int(str(-1*x)[::-1])

        if abs(a) > (2**31 - 1):
            return 0
        else:
            return a


if __name__ == '__main__':
    print(Solution().reverse(-12222222))