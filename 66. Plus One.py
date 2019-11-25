class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        return ( [x for x in str(int("".join(map(str,digits)))+1)] )

if __name__ == '__main__':
    print(Solution().plusOne([1,2,3]))