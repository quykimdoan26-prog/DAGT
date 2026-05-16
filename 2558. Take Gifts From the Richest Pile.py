import heapq
import math


class Solution:

    def pickGifts(self, gifts: list[int], k: int) -> int:
        # Bước 1: Biến đổi mảng thành Max-Heap bằng cách đổi dấu các phần tử
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        # Bước 2: Thực hiện hành động trong k giây
        for _ in range(k):
            # Lấy ra đống quà lớn nhất (được lưu dưới dạng số âm nhỏ nhất)
            largest = -heapq.heappop(max_heap)

            # Tính số quà mới sau khi lấy căn bậc hai và làm tròn xuống
            remaining = math.floor(math.sqrt(largest))

            # Đẩy giá trị mới trở lại vào heap (nhớ đổi lại dấu âm)
            heapq.heappush(max_heap, -remaining)

        # Bước 3: Tính tổng số quà còn lại (đổi lại dấu dương)
        return -sum(max_heap)