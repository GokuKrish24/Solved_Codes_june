class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        lcs=[]
        mac=0
        ans=""
        for i in range(n):
            lcs.append([0]*(n))
        for i in range(n-1):
            lcs[i][i]=1
            if(s[i]==s[i+1]):
                lcs[i][i+1]=1
                mac=2
                ans=s[i:i+2]
        lcs[n-1][n-1]=1

        for i in range(2,n):
            for j in range(0,n-2):
                if(j+i<n and j+1<n and s[j]==s[j+i] and lcs[j+1][j+i-1]):
                    lcs[j][j+i]=1
                    if(i+1>mac):
                        mac=i+1
                        ans=s[j:j+i+1]

        if(len(ans)==0):
            return s[0]
        return ans
