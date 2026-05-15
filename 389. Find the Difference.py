class Solution(object):
    def findTheDifference(self, s, t):
        counter_s = Counter(s)
        counter_t = Counter(t)
        
        for ch in counter_t:
            if counter_t[ch] != counter_s.get(ch, 0):
                return ch
        return " "
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        