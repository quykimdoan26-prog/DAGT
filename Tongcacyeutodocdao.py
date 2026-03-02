from collections import Counter
class Solution(object):
    def sumOfUnique(self, nums):
        count=Counter(nums)
        d=[x for x in nums if count[x]<2]
        return sum(d)
        """
        :type nums: List[int]
        :rtype: int
        """