def reverseWords(self, s: str) -> str:
        ns=""
        p=""
        for i in range(len(s)):
            if(len(p)!=0 and s[i]==" "):
                print(p,ns)
                ns=p+" "+ns
                p=""
            else:
                if(s[i]!=" "):
                    p+=s[i]
        if(len(p)!=0):
            ns=p+" "+ns
        return ns[:len(ns)-1]
