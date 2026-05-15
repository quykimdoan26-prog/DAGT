class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        chai=0
        empty=0
        while  numBottles>0:
            chai+=numBottles
            empty+=numBottles
            numBottles=empty//numExchange
            empty=empty%numExchange
        return chai