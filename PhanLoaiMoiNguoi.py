class Solution(object):
    def sortPeople(self, names, heights):
        d={}
        j=0
        for i in heights:
            d[i]=names[j] #chiều cao của mỗi người {158:quý}
            j+=1
        items = sorted(d.items(), key=lambda x: x[0], reverse=True) # ép thành list-> chiều cao đã được sắp xếp từ lớn xuống bé
        return [x[1] for x in items]
    
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """