class Solution(object):
    def replaceDigits(self, s):
        res = []
        for i, ch in enumerate(s):
            if i % 2 == 0:  # vị trí chẵn: chữ cái giữ nguyên
                res.append(ch)
            else:           # vị trí lẻ: chữ số → shift
                prev = res[-1]
                shift_val = int(ch)
                res.append(chr(ord(prev) + shift_val))
        return "".join(res)


        

        """
        :type s: str
        :rtype: str
        """
        