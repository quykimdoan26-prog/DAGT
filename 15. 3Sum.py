class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Bước 1: Sắp xếp mảng tăng dần
        nums.sort()

        # Duyệt qua từng số để làm mốc cố định thứ nhất (nums[i])
        for i in range(len(nums) - 2):
            # Bỏ qua các phần tử trùng lặp cho vị trí thứ nhất
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Sử dụng kỹ thuật 2 con trỏ cho phần mảng còn lại bên phải
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    # Tổng nhỏ quá, cần tăng giá trị lên -> dịch con trỏ trái sang phải
                    left += 1
                elif total > 0:
                    # Tổng lớn quá, cần giảm giá trị đi -> dịch con trỏ phải sang trái
                    right -= 1
                else:
                    # Tìm thấy một bộ ba thỏa mãn tổng bằng 0
                    res.append([nums[i], nums[left], nums[right]])

                    # Bỏ qua các phần tử trùng lặp cho con trỏ 'left'
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Bỏ qua các phần tử trùng lặp cho con trỏ 'right'
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Sau khi bỏ qua trùng lặp, dịch chuyển tiếp cả 2 con trỏ
                    left += 1
                    right -= 1

        return res