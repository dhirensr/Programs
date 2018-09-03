def candy1(n):
    len_n=len(n)
    max_n= max(n)
    avg = sum(n)/len_n
    if(avg.is_integer()):
        counter=0
        for i in n:
            if(i< int(avg)):
                counter+= (int(avg)-i)
        print(counter)
    else:
        print(-1)
t=1
while(t>0):
    n=input()
    if(int(n)!=-1):
        a=[]
        for i in range(int(n)):
            a.append(int(input()))
        candy1(a)
    else:
        t=-1
        break
