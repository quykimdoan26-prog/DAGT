class Solution(object):
    def topKFrequent(self, nums, k):
        d={}
    # dùng vòng lặp lưu tần số xuất hiện của các số trong " nums" -> {1:2,2:1}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                 d[i]=1
        items = sorted(d.items(), key=lambda x: x[1], reverse=True) # items là một list ->[(1,2),(2,1)] =>
    #=> được sắp xếp theo tần số xuất hiện từ lớn đến nhỏ (x[1] là tần số x[0] là giá trị)
        l=[]
        for i in range(k):
            l.append(items[i][0])
        return l
        

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        