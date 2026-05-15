class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        x=[]
        for i in range(len(nums)):
            if nums[i]==target:
                x.append(i)
        return x


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        