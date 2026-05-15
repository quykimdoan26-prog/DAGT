class Solution(object):
    def checkValid(self,matrix):
        n = len(matrix)
    
        for i in range(n):
            row_set = set()
            col_set = set()
            for j in range(n):
            # Kiểm tra hàng i
                if matrix[i][j] in row_set:
                    return False
                row_set.add(matrix[i][j])
            
                # Kiểm tra cột i (đổi chỉ số để duyệt theo cột)
                if matrix[j][i] in col_set:
                    return False
                col_set.add(matrix[j][i])
            
        return True
        

    """
        :type matrix: List[List[int]]
        :rtype: bool
    """
        