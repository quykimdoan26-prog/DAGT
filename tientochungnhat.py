def longestCommonPrefix(self, strs):
    if not strs:
        return ""
    #strs = ["flower","flow","flight"]
    #khởi tạo tiền tô chung ban đầu là từ đầu tiên trong ds, để kiểm tra.
    prefix=strs[0]
    for i in strs[1:]:
        while not i.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix:
                return " "
    return prefix
        

    

        