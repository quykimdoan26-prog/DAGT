class Solution(object):
    def divideArray(self, nums):
        counts={}
        if len(nums)%2==0:
            for i in nums:
                counts[i]= counts.get(i, 0) + 1
            for i in counts:
                if counts[i]%2!=0:
                    return False
        else: return False
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        