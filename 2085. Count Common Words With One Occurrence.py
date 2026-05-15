class Solution(object):
    def countWords(self, words1, words2):
        cout=Counter(words1)
        cout2=Counter(words2)
        sum=0
        if len(words1)> len(words2):
            for i in words1:
                if cout[i]==1 and cout2[i]==1:
                    sum+=1
        else:
            for i in words1:
                if cout[i]==1 and cout2[i]==1:
                    sum+=1
        return sum

        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        