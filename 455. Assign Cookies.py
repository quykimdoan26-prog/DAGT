class Solution(object):
    def findContentChildren(self, g, s):
        g.sort() # Sắp xếp trẻ em tăng dần
        s.sort() # Sắp xếp bánh quy tăng dần
        
        child_i = 0
        cookie_j = 0
        
        # Chạy đến khi hết trẻ hoặc hết bánh
        while child_i < len(g) and cookie_j < len(s):
            # Nếu bánh đủ lớn cho trẻ
            if s[cookie_j] >= g[child_i]:
                child_i += 1  # Đứa trẻ này đã hài lòng
            
            # Luôn chuyển sang chiếc bánh tiếp theo (vì bánh hiện tại 
            # hoặc đã được ăn, hoặc quá nhỏ không dùng được nữa)
            cookie_j += 1
            
        return child_i
                
           



        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        