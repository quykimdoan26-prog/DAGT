class Solution(object):
    def plusOne(self, digits):
        result = int("".join(str(x) for x in digits ))
        result+=1
        d=[]
        for i in str(result):
            d.append(int(i))
        return d

        """
        :type digits: List[int]
        :rtype: List[int]
        """
        