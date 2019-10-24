class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[len(x)-1-i]:
                return False
        return True

    # Reverse number method
    """ 
        s = 0
        o = x
        print(type(x),type(s))
        if x < 0:
            return False
        while (x != 0):
            s = s * 10 + x % 10
            x = x // 10
        
        return s - o == 0
    """

if __name__ == '__main__':
    print(Solution().isPalindrome(121))