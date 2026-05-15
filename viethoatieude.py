class Solution(object):
    def capitalizeTitle(self, title):
        d=title.split()
        x=[]
        for i in range(len(d)):
            if len(d[i])>2:
                c=d[i].title()
                x.append(c)
            else:
                c=d[i].lower()
                x.append(c)
        return " ".join(x)
