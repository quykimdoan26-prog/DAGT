class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip() # xóa dấu cách đầu cuối
        d=s.split(" ") # tạo danh sach các từ được ngăn cách bởi dấu cách trong chuỗi s
        return len(d[-1]) # trả về độ dài từ cuối cùng
        """
        :type s: str
        :rtype: int
        """