class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True) #[2.2.5.6.7.9]
        sum=0
        for i in range(len(cost)):
            if ((i+1)%3)==0:
                continue
            sum+=cost[i]
        return sum


        """
        :type cost: List[int]
        :rtype: int
        """
        