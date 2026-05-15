class Solution(object):
    def lemonadeChange(self, bills):
        tien=0
        chuc=0
        for i in bills:
            if i==5:
                tien+=1
            elif i>5:
                if i==10:
                    if tien>=1:
                        tien-=1
                        chuc+=1
                    else:
                        return False  
                else: 
                    if tien>=1 and chuc>=1:
                        tien-=1
                        chuc-=1
                    elif tien>=3:
                        tien-=3
                    else:
                       return False
        return True