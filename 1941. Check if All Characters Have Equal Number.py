class Solution(object):
    def areOccurrencesEqual(self, s):
        count=Counter(s) # đếm số lần xuất hiện
        d=s[0]
        for i in set(s):
            if count[i]!=count[d]:
                return False
        return True
            


        """
        :type s: str
        :rtype: bool
        """
        