class Solution(object):
    def reformatNumber(self, number):
        # B1: Lọc ra các chữ số
        digits = [ch for ch in number if ch.isdigit()]
        s = "".join(digits)

        res = []
        i = 0
        n = len(s)

        # B2: Chia khối 3 cho đến khi còn <= 4 chữ số
        while n - i > 4:
            res.append(s[i:i+3])
            i += 3

        # B3: Xử lý phần còn lại
        if n - i == 4:
            res.append(s[i:i+2])
            res.append(s[i+2:i+4])
        else:
            res.append(s[i:])

        # B4: Ghép lại bằng dấu '-'
        return "-".join(res)

        """
        :type number: str
        :rtype: str
        """
        