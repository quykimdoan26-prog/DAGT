class Solution(object):
    def canPlaceFlowers(self, fl, n):
        t=len(fl)
        for i in range(t): # lặp từ đầu đến cuối
            if fl[i]==0: # số ở thứ i=0 thì kiểm tra trái phải 
                kt_left= i==0 or fl[i-1]==0
                kt_right=i==t-1 or fl[i+1]==0
                if kt_left and kt_right: # nếu trái phải đều là đất trống(=0) thì trồng thêm hoa
                    fl[i]=1 # cắm vào đất
                    n-=1 # -1 bông
                    if n == 0:   # dừng ngay khi đủ hoa
                        return True
        return n <= 0


        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        