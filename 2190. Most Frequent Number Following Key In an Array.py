class Solution(object):
    def mostFrequent(self, nums, key): # Thêm 'self' vào đây
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        counts = {}
        max_count = 0
        target = 0 # Nên khởi tạo là 0 hoặc số nguyên theo yêu cầu đề bài

        # Duyệt qua mảng đến phần tử kế cuối
        for i in range(len(nums) - 1):
            # Nếu phần tử hiện tại là 'key'
            if nums[i] == key:
                follow = nums[i + 1]
                # Cập nhật số lần xuất hiện
                counts[follow] = counts.get(follow, 0) + 1
                
                # Kiểm tra xem đây có phải là số xuất hiện nhiều nhất không
                if counts[follow] > max_count:
                    max_count = counts[follow]
                    target = follow
                    
        return target
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        