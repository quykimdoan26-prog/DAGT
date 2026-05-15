class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        words = re.findall(r'\w+', paragraph.lower())
        count = Counter(words)
        
        # duyệt theo tần suất giảm dần
        for word, freq in count.most_common():
            if word not in banned:
                return word
        return ""
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        