class Solution(object):
    def distributeCandies(self, candies, num_people):
        d=[0]*num_people
        keo=1
        while candies>0:
            for i in range(num_people):
                if keo<=candies:
                    d[i]+=keo
                    candies-=keo
                    keo+=1
                else:
                    d[i]+=candies
                    candies-=candies
        return d
    


