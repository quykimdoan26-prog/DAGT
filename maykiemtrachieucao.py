class Solution(object):
    def heightChecker(self, heights):
        d=sorted(heights)
        sum=0
        x=0
        for i in d:
            if i!=heights[x]:
                sum+=1
            x+=1

        return sum 


        """
        :type heights: List[int]
        :rtype: int
        """