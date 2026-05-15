class Solution(object):
    def sortPeople(self, names, heights):
        d={}
        j=0
        for i in heights:
            d[i]=names[j]
            j+=1
        items = sorted(d.items(), key=lambda x: x[0], reverse=True)
        return [x[1] for x in items]

        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        