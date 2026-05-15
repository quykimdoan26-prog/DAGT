class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        sum=0
        for i in stones:
            if i in  jewels:
              sum+=1
        return sum

        
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        