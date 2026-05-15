class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        t=0
        for i in range(len(timeSeries)-1):
            t+=min(timeSeries[i+1]-timeSeries[i],duration)
        t+=duration
        return t

           
            


        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        