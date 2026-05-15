class Solution(object):
    def thousandSeparator(self, n):
        x=str(n)
        d=list(x)
        i=len(d)-3
        while i>0:
            d.insert(i,".")
            i-=3
        return "".join(d)




        """
        :type n: int
        :rtype: str
        """
        