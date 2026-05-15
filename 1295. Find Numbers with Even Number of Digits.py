class Solution(object):
    def findNumbers(self, nums):
        sum=0
        for i in nums:
            if len(str(i))%2==0:
                sum+=1
        return sum 
        
        """
        :type nums: List[int]
        :rtype: int
        """
        