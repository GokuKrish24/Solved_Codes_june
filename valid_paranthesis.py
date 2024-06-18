class Solution:
    def isValid(self, s: str) -> bool:
        arr=["-1"]
        flag=0
        for i in range(len(s)):
            if(s[i]=="(" or s[i]=="[" or s[i]=="{"):
                arr.append(s[i])
            else:
                if((arr[len(arr)-1]=="[" and s[i]=="]") or (arr[len(arr)-1]=="(" and s[i]==")") or (arr[len(arr)-1]=="{" and s[i]=="}")):
                    arr.pop()
                else:
                    flag=1
                    break
        if(flag==1 or len(arr)!=1):
            return False
        return True
