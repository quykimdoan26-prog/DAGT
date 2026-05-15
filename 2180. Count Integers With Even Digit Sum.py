class Solution(object):
    def countEven(self, num):
        count=0
        for i in range(1,num+1):
            x=i
            dem=0
            while(x!=0):
                dv=x%10
                dem+=dv
                x//=10
            if(dem%2==0):
                count+=1
            
        return count

        """
        :type num: int
        :rtype: int
        """
        