class Solution(object):
    def sortEvenOdd(self, nums):
        # 1. Tách các phần tử ở vị trí chẵn và lẻ
            even = nums[::2]
            odd = nums[1::2]
            
            # 2. Sắp xếp theo yêu cầu
            even.sort()             # Tăng dần cho chỉ số chẵn
            odd.sort(reverse=True)  # Giảm dần cho chỉ số lẻ
            
            # 3. Gộp lại vào mảng kết quả
            res = [0] * len(nums)
            res[::2] = even
            res[1::2] = odd
            
            return res
            """
            :type nums: List[int]
            :rtype: List[int]
            """
        