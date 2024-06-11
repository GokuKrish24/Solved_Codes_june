def JobScheduling(Jobs,n): #Jobs here is array of objects
        Jobs.sort(key=lambda x:x.profit,reverse=True)
        mx=0
        for i in range(n):
            mx=max(mx,Jobs[i].deadline)
        L=[-1 for i in range(mx+1)]
        tp=0
        cnt=0
        for i in range(n):
              if(L[Jobs[i].deadline]==-1):
                    tp+=Jobs[i].profit
                    cnt+=1
                    L[Jobs[i].deadline]=Jobs[i].id
              else:
                    j=Jobs[i].deadline-1
                    while(j>0):
                          if(L[j]==-1):
                                tp+=Jobs[i].profit
                                cnt+=1
                                L[j]=Jobs[i].id
                                break
                          j-=1
        return [cnt,tp]
