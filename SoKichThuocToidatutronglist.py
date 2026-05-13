class Solution(object):
    def mostWordsFound(self, sentences):
        maxl=0
        for i in sentences:
            x=i.split()
            maxl=max(maxl,len(x))
        return maxl

        """
        :type sentences: List[str]
        :rtype: int
        """
        