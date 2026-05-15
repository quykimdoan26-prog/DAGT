class Solution(object):
    def distributeCandies(self, candyType):
        d=set(candyType)
        sum=0
        if len(d)>=len(candyType)/2:
            sum+=len(candyType)/2
        else:
            sum+=len(d)
        return sum

          
        """
        :type candyType: List[int]
        :rtype: int
        """
        