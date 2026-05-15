def prefixCount(self, words, pref):
        count=0
        for i in words:
            if(i[0:len(pref)]==pref): count+=1

        return count