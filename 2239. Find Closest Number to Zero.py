class Solution:

    def findClosestNumber(self, nums: list[int]) -> int:
        # Khởi tạo giá trị gần 0 nhất là phần tử đầu tiên của mảng
        closest = nums[0]

        for num in nums:
            # Nếu khoảng cách của số hiện tại tới 0 nhỏ hơn số 'closest' hiện tại
            if abs(num) < abs(closest):
                closest = num
            # Nếu khoảng cách bằng nhau, chọn số có giá trị lớn hơn
            elif abs(num) == abs(closest):
                if num > closest:
                    closest = num

        return closest