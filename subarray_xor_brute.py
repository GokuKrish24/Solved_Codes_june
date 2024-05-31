arr=[4, 2, 2, 6, 4]

cnt=0
# for i in range(len(arr)):
#     for j in range(len(arr)-i+1):
#         xor=0
#         for k in range(j,j+i):
#             print(arr[k],end=" ")
#             xor^=arr[k]
#             if(xor==6):
#                 cnt+=1
#                 print(cnt)

#         print()

for i in range(len(arr)):
    xor=0
    for j in range(i,len(arr)):
        xor^=arr[j]
        if(xor==6):
            cnt+=1
print(cnt)


'''
100

----
110


'''
