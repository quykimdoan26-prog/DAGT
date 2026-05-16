from collections import Counter


class Solution:

    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        # Bước 1: Tính tất cả các tổng có thể của (nums1[i] + nums2[j])
        # và đếm số lần xuất hiện của mỗi tổng bằng Counter
        sum_ab = Counter(a + b for a in nums1 for b in nums2)

        count = 0

        # Bước 2: Duyệt qua tất cả các cặp của nums3 và nums4
        for c in nums3:
            for d in nums4:
                # Tìm tổng đối nghịch của (c + d) trong bảng băm
                target = -(c + d)
                if target in sum_ab:
                    count += sum_ab[target]

        return count