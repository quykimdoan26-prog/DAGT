class Solution(object):
    def findFinalValue(self, nums, original):
        nums.sort()
        for num in nums:
            if num ==original:
                original *= 2
        return original
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        