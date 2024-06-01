S="takeuforward"
st=set()
l=0
cnt=0
for i in range(len(S)):
    if(S[i] in st):
        while(l<i and S[i] in st):
            st.remove(S[l])
            l+=1
    st.add(S[i])
    cnt=max(cnt,i-l+1)
print(cnt)

'''
O(n) solution
def lengthOfLongestSubstring(self, s: str) -> int:
        L=[-1]*256
        cnt=0
        l=0
        for i in range(len(s)):
            if(L[ord(s[i])] != -1):
                l=max(l,L[ord(s[i])]+1)
            cnt=max(cnt,i-l+1)
            L[ord(s[i])]=i
        return cnt


'''
