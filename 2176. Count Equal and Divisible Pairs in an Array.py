class Solution(object):
    def countPairs(self, nums, k):
        index_map = {}
        total = 0

        for i, value in enumerate(nums):
            if value in index_map:
                for prev_index in index_map[value]:
                    if ((i * prev_index) % k == 0):
                        total += 1
                index_map[value].append(i)
            else:
                index_map[value] = [i]

        return total
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        