class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        elif len(haystack) < len(needle):
            return -1

        offset = len(haystack) - len(needle) + 1

        for i in range(offset):
            print(haystack[i:i + len(needle)])
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().strStr("Hello","ll"))