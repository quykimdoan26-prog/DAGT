class Solution(object):
    def prefixCount(self, words, pref):
        count=0
        for i in words:
            if(i[0:len(pref)]==pref): count+=1

        return count
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        