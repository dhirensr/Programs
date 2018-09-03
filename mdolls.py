import operator
def mdolls(d,n):
    v=[]
    v.append(d[0])
    for i in range(1,n):
        lo=0
        hi=len(v)-1
        while(lo <=hi):
            mid=int(lo+hi/2)
            if(v[mid][0] > d[i][0] and v[mid][1]!=d[i][1]):
                hi=mid-1
            else:
                lo=mid+1
        if(lo==len(v)):
            v.append(d[i])
        else:
            v[lo][0] = d[i][0]
            v[lo][1] = d[i][1]
    return len(v)




t=input()
for i in range(int(t)):
    n=input()
    d=[]
    dolls=[int(i) for i in input().split()]
    for j in range(0,len(dolls),2):
        d.append([dolls[j+1],dolls[j]])
    d=sorted(d,key=operator.itemgetter(0,1),reverse=True)
    print(mdolls(d,int(n)))
