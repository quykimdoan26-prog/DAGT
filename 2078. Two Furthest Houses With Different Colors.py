class Solution(object):
    def maxDistance(self, colors):
        c=0
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    c=max(c,j-i)
        return c


        """
        :type colors: List[int]
        :rtype: int
        """
        