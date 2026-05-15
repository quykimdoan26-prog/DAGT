class Solution(object):
    def firstUniqChar(self, s):
        count = Counter(s)  # Đếm số lần xuất hiện
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1



        
            


        """
        :type s: str
        :rtype: int
        """
        