class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                return [d[target - nums[i]],i]

        return -1


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15],9))