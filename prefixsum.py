
nums=[1,2,3]
k=3
prefix={0:1}
prefixsum=0
count=0
for i in range(len(nums)):
    prefixsum+=nums[i]
    if(prefixsum-k in prefix):
        count+=prefix[prefixsum-k]
    if prefixsum not in prefix:
        prefix[prefixsum]=0
    prefix[prefixsum]+=1
print(count)
