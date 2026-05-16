class Solution:

    def maxArea(self, height: list[int]) -> int:
        # Khởi tạo hai con trỏ ở hai đầu mảng
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Tính chiều rộng giữa hai con trỏ
            width = right - left

            # Chiều cao của bể chứa quyết định bởi cột thấp hơn
            current_height = min(height[left], height[right])

            # Tính lượng nước hiện tại và cập nhật kỷ lục max_water
            current_water = width * current_height
            max_water = max(max_water, current_water)

            # Chiến lược di chuyển con trỏ:
            # Luôn di chuyển con trỏ đang đứng ở cột thấp hơn
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water