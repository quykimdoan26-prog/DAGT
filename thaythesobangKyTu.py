class Solution(object):
    def replaceDigits(self, s):
        res = []
        for i, ch in enumerate(s):
            if i % 2 == 0:  # vị trí chẵn: chữ cái giữ nguyên
                res.append(ch)
            else:           # vị trí lẻ: chữ số → shift
                prev = res[-1] # lấy từ hiện tại trong list
                shift_val = int(ch)
                res.append(chr(ord(prev) + shift_val))  # ép số thành chữ tương ứng: lấy số chữ hiện tại +số trong mảng
        return "".join(res)


        

        """
        :type s: str
        :rtype: str
        """
# bỏ qua các chữ, sữa các số thành chữ tương ứng với tổng số chữ cái trước với số đó
class Solution(object):
    def replaceDigits(self, s):
        res = list(s)
        for i in range(1, len(s), 2):
            res[i] = chr(ord(s[i-1]) + int(s[i]))
        return "".join(res)
        """
        :type s: str
        :rtype: str
        """
        