class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote) # hàm tạo dictionary , đếm số lần xuất hiện của từng phần tử
        magazine_count = Counter(magazine)
        for char, cnt in ransom_count.items(): #lặp ds ransom,items()-> tạo list từ các cặp trong dic.
            if magazine_count[char] < cnt: # nếu số lượng chữ cái trong magazine ít hơn thì trả về sai 
                return False
        return True # còn không thì đúng 

        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        