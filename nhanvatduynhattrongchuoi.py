from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        count = Counter(s)  # Đếm số lần xuất hiện
        for i, ch in enumerate(s):# lấy lần lượt index, và giá trị tại index đó 
            if count[ch] == 1:
                return i
        return -1