class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not str or len(strs) == 0:
            return ""

        # Vertical scan
        ref = strs[0]
        # Each character in the reference string
        for i in range(len(ref)):
            c = ref[i]
            # each string
            for s in range(1,len(strs)):
                if i == len(strs[s]) or strs[s][i] != c:
                    return ref[0:i]
        return ref

    def longestCommonPrefixBinarySearch(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        def isCommonPrefix(strs,l):
            ref = strs[0][0:l+1]
            for i in range(1,len(strs)):
                if not strs[i].startswith(ref):
                    return False
            return True

        if not str or len(strs) == 0:
            return ""

        m = len(min(strs,key=len))
        low = 0
        high = m - 1

        while (low < high):
            mid = (high + low) // 2
            if isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid
        return strs[0][0:(high + low) // 2]