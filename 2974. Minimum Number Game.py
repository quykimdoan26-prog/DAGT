class Solution:

    def numberGame(self, nums: list[int]) -> list[int]:
        # Bước 1: Sắp xếp mảng theo thứ tự tăng dần
        nums.sort()

        # Bước 2: Duyệt qua mảng với bước nhảy là 2 để xử lý từng cặp
        for i in range(0, len(nums), 2):
            # Hoán đổi vị trí giữa số của Alice (nums[i]) và Bob (nums[i+1])
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums