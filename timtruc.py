class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)        # 1. Tính tổng toàn bộ mảng
        left_sum = 0             # 2. Khởi tạo tổng bên trái = 0
        for i, num in enumerate(nums):   # 3. Duyệt từng phần tử với index i và giá trị num
            # 4. Kiểm tra điều kiện pivot:
            #    tổng bên trái == tổng bên phải
            #    tổng bên phải = total - left_sum - num
            if left_sum == total - left_sum - num:
                return i         # Nếu thỏa mãn, trả về index i ngay
            left_sum += num      # 5. Cập nhật tổng bên trái (thêm phần tử hiện tại)
        return -1                # 6. Nếu duyệt hết không tìm thấy, trả về -1