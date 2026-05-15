class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l=0
        d=[]
        for i in range(len(nums)):
            if nums[i]==1:
                l+=1
            else:
                d.append(l)
                l=0
            if i==len(nums)-1:
                 d.append(l)
        return max(d)
    