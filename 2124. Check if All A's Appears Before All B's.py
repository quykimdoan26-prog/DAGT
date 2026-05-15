class Solution(object):
    def checkString(self, s):
        r= ""
        for i in range(len(s)):
            if s[i]=="a":
                continue
            else:
                r+=s[i:]
                break
        for i in r:
            if i=="a":
                return False 
        return True

        """
        :type s: str
        :rtype: bool
        """
        