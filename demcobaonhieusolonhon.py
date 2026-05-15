class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums) # sắp xếp lại mảng
        rank = {} # tạo dict số số bé hơn 
        # vói mảng [8,4,5,9] =>[4,5,8,9] => với từng số, số index lại là số số bé hơn số đó
        for i, num in enumerate(sorted_nums): # lấy index và số tại đó
            if num not in rank: 
                rank[num] = i # gán vào dict
        
        return [rank[num] for num in nums] # trả về list các số số bé hơn trong dicct