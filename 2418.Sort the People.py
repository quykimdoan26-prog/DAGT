class Solution:

    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        # Gộp heights và names lại thành các cặp (chiều cao, tên)
        # Ví dụ: [(180, "Mary"), (165, "John"), (170, "Emma")]
        people = list(zip(heights, names))

        # Sắp xếp giảm dần (reverse=True) dựa trên phần tử đầu tiên của bộ (chiều cao)
        people.sort(reverse=True)

        # Trích xuất lại danh sách tên sau khi đã sắp xếp
        return [name for height, name in people]