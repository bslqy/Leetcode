class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        res = []

        for i in range(length - 2):
            if nums[i] == 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i + 1,length - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r-= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append((nums[i],nums[l],nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l < r and nums[r-1] == nums[r]:
                        r-=1

                    r-= 1
                    l+= 1
        return res



if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))