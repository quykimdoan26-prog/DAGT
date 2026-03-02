import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        # loại bỏ dấu câu, chuyển về chữ thường
        words = re.findall(r'\w+', paragraph.lower()) # ép thành list các từ trong " paragraph"
        count = Counter(words) # đếm số lần xuất hiện
        # duyệt theo tần suất giảm dần
        for word, freq in count.most_common(): #most_common():phổ biến nhất trả về {từ: tần số}
            if word not in banned: # không có trong từ cấm => true
                return word
        return ""
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """