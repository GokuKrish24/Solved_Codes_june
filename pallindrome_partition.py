def pallindrome(s):
    res=[]
    path=[]
    def pali(s,ind):
        if(ind==len(s)):
            res.append(path[:])
            return
        for i in range(ind,len(s)):
            if(s[ind:i+1]==s[ind:i+1][::-1]):
                path.append(s[ind:i+1])
                pali(s,i+1)
                path.pop()
    pali(s,0)
    return res
print(pallindrome("aab"))
