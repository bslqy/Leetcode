class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            elif i in s:
                return True
        return False



if __name__ == '__main__':
    print(Solution().containsDuplicate([-2,1,-3,4,-1,2,1,-5,4]))