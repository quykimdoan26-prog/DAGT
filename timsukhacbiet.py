from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        counter_s = Counter(s) # đếm số lần xuất hiện của các chữ cái trong 2 chuỗi 
        counter_t = Counter(t)
        for ch in counter_t:
            if counter_t[ch] != counter_s.get(ch, 0): # nếu số lần xhien của 1 kí tự trong t!=s
                # thì trả về kí tự đó là sự khác biệt
                return ch
        return " "
        """
        :type s: str
        :type t: str
        :rtype: str
        """