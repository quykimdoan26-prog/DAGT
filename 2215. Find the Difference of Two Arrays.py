class Solution:

    def findDifference(
        self, nums1: list[int], nums2: list[int]
    ) -> list[list[int]]:
        # Chuyển đổi hai mảng thành tập hợp để loại bỏ trùng lặp
        set1 = set(nums1)
        set2 = set(nums2)

        # set1 - set2: lấy các phần tử thuộc set1 nhưng không thuộc set2
        # set2 - set1: lấy các phần tử thuộc set2 nhưng không thuộc set1
        ans0 = list(set1 - set2)
        ans1 = list(set2 - set1)

        return [ans0, ans1]