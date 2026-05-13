class Solution(object):
    def minimumSum(self, num):
        nums=[int(i) for i in (str(num))]
        nums.sort()
        x=str(nums[0])+str(nums[2])
        y=str(nums[1])+str(nums[3])   
        if(int(x)%10==0):
            x=nums[0]
        if(int(y)%10==0):
            y=nums[1]
        return int(x)+int(y)

        """
        :type num: int
        :rtype: int
        """
        