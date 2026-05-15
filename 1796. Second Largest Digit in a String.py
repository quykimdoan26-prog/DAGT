class Solution(object):
    def secondHighest(self, s):
        d=[x for x in s if x.isdigit()]
        x = sorted(set(d), reverse=True)         # loại trùng + sắp xếp giảm dần
        if len(x) > 1:
            return int(x[1])                
        else:
            return -1


        """
        :type s: str
        :rtype: int
        """
        