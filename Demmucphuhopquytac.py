class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        sum=0
        if ruleKey=="color":
            lay=1
        elif ruleKey=="type":
            lay=0
        else:
            lay=2
        for i in items:
            if i[lay]==ruleValue:
                sum+=1
        return sum

        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
