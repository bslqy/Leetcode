class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # sort
        res = []
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            for j in range(i + 1, length - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                l, r = j + 1, length - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:  # [6]
                            r -= 1
                        l += 1
                        r -= 1
        return set(res)

    def fourSumHashMap(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = dict()
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if nums[i] + nums[j] in d:
                    d[nums[i] + nums[j]].append((i,j))
                else:
                    d[nums[i] + nums[j]] = [(i,j)]

        # right hand side
        res = set()
        for key in d:
            value = target - key
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i,j) in list1:
                    for (k,l) in list2:
                        if i!=k and i!=l and j!=k and j!=l:
                            flist = [nums[i],nums[j],nums[k],nums[l]]
                            flist.sort()
                            res.add(tuple(flist))

        return res



if __name__ == '__main__':
    print(Solution().fourSumHashMap([1,0,-1,0,-2,2],0))
