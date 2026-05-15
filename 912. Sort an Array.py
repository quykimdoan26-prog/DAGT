class Solution(object):
    def sortArray(self, nums):
        def heapify(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            # nếu con trái lớn hơn gốc
            if left < n and nums[left] > nums[largest]:
                largest = left

            # nếu con phải lớn hơn gốc
            if right < n and nums[right] > nums[largest]:
                largest = right

            # nếu gốc không phải lớn nhất, hoán đổi và tiếp tục heapify
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        n = len(nums)

        # xây dựng max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # trích xuất từng phần tử từ heap
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # hoán đổi gốc với phần tử cuối
            heapify(nums, i, 0)  # heapify lại phần còn lại

        return nums

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        