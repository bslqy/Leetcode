class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        local = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            local = max(local + nums[i], nums[i])
            res = max(res,local)

        return res



if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))