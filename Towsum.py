def kiemtra(ls,target):
    d={}
    for i in range(len(ls)):
        if target-ls[i] in d:
            return [d[target-ls[i]],i]
        d[ls[i]]=i
    return " "

ls=[2,7,58,77]
x=9
print(kiemtra(ls,x))