class Solution(object):
    def distributeCandies(self, candyType):
        d=set(candyType) # xác định có bao nhiêu loại kẹo
        sum=0
        if len(d)>=len(candyType)/2: # số kẹo có lớn hơn hoặc bằng sl cho phép thì lấy hết = sl cho phép
            sum+=len(candyType)/2
        else: # nếu bé hơn số lượng cho phép thì lấy hết số kẹo có được là ok 
            sum+=len(d)
        return sum # trả về số kẹo lấy được 

        """
        :type candyType: List[int]
        :rtype: int
        """