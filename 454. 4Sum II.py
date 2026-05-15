class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        from collections import defaultdict
        count = defaultdict(int)
        
        # Bước 1: lưu tổng của nums1 + nums2
        for a in nums1:
            for b in nums2:
                count[a+b] += 1
        
        res = 0
        # Bước 2: kiểm tra tổng của nums3 + nums4
        for c in nums3:
            for d in nums4:
                res += count[-(c+d)]
        
        return res
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        