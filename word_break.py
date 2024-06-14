def wordBreak(s, dictionary):
    des=[]
    def breaking(s,ind,dictionary):
        if(ind==len(s)):
            for i in range(len(des)):
                if(i==len(des)-1):
                    print(des[i])
                else:
                    print(des[i],end=" ")
            return
        for i in range(ind,len(s)):
            if(s[ind:i+1] in dictionary):
                des.append(s[ind:i+1])
                breaking(s,i+1,dictionary)
                des.pop()
        return
    breaking(s,0,dictionary)

wordBreak("godisnowhere",["god","is","no","here"])
