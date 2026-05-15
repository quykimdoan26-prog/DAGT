
def canPlaceFlowers( fl, n):
    t=len(fl)
    for i in range(t): # lặp từ đầu đến cuối
        if fl[i]==0: # số ở thứ i=0 thì kiểm tra trái phải 
            kt_left= i==0 or fl[i-1]==0
            kt_right=i==t-1 or fl[i+1]==0
            if kt_left and kt_right: # nếu trái phải đều là đất trống(=0) thì trồng thêm hoa
                fl[i]=1
                n-=1 # -1 bông
                if n==0:
                    return True
    return n<=0


if canPlaceFlowers([1,0,0,0,0,0,0,1],2):
    print("trồng đủ")
else:
    print("không trồng đủ")