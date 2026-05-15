class Solution(object):
    def isSubsequence(self, s, t):
        i = 0  # con trỏ cho s
        for ch in t:   # duyệt từng ký tự trong t
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)

        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        