class Solution(object):
    import math
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = -(-len(B) // len(A))
        for i in range(2):
            if B in A * (times + i):
                return times + i
        return -1
if __name__ == '__main__':
    print(Solution().repeatedStringMatch("abcd","cdabcdab"))