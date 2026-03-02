class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                # Chèn số 0 vào vị trí i + 1
                arr.insert(i + 1, 0)
                # Xóa phần tử cuối cùng để giữ nguyên độ dài mảng
                arr.pop()
                # Nhảy qua số 0 vừa được chèn
                i += 2
            else:
                i += 1
