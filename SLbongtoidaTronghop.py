class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        lst = [0] * 46
        for i in range(lowLimit, highLimit + 1):
            sm = 0
            while i:
                sm = sm + i % 10
                i =i // 10
            lst[sm] += 1
        return max(lst)