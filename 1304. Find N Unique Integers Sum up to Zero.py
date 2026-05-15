class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        
        # Duyệt từ 1 đến n // 2 để tạo các cặp đối xứng
        for i in range(1, (n // 2) + 1):
            res.append(i)
            res.append(-i)
            
        # Nếu n là số lẻ, ta thêm số 0 vào để đủ số lượng phần tử
        if n % 2 != 0:
            res.append(0)
            
        return res


        """
        :type n: int
        :rtype: List[int]
        """
        