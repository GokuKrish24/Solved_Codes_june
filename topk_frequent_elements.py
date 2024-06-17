def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            if(nums[i] in dic):
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        k1=list(dic.items())
        k1.sort(key=lambda x:x[1], reverse=True)
        ans=[]
        for i in range(k):
            ans.append(k1[i][0])
        return ans
