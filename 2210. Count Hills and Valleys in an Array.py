class Solution:

    def countHillValley(self, nums: list[int]) -> int:
        # Bước 1: Loại bỏ các phần tử trùng nhau liên tiếp
        unique_nums = []
        for num in nums:
            if not unique_nums or num != unique_nums[-1]:
                unique_nums.append(num)

        count = 0
        # Bước 2: Duyệt qua các phần tử bên trong (bỏ phần tử đầu và cuối)
        for i in range(1, len(unique_nums) - 1):
            # Kiểm tra nếu là đỉnh đồi (lớn hơn 2 bên)
            if (
                unique_nums[i] > unique_nums[i - 1]
                and unique_nums[i] > unique_nums[i + 1]
            ):
                count += 1
            # Kiểm tra nếu là thung lũng (nhỏ hơn 2 bên)
            elif (
                unique_nums[i] < unique_nums[i - 1]
                and unique_nums[i] < unique_nums[i + 1]
            ):
                count += 1

        return count