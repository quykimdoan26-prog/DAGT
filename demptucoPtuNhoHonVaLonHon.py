from collections import Counter
class Solution(object):
    def countElements(self, nums):
        count=Counter(nums)
        x=sorted(set(nums),reverse=True) # [2,7,11,15] 
        sum=0
        for i in x[1:len(x)-1]:
            sum+=count[i]

        return sum
        """
        :type nums: List[int]
        :rtype: int
        """