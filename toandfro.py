def to_and_fro(n,pattern):
    loop_range=len(pattern)//n
    str1=''
    str2=''
    for i in range(loop_range):
        if(i %2==1):
            str1+=(pattern[i*n:(i+1)*n][::-1])
        else:
            str1+=(pattern[i*n:(i+1)*n])
    for i in range(n):
        str2+=str1[i::n]
    print(str2)


i=0
while(i!=-1):
    t=input()
    s=int(t)
    if(s==0):
        i=-1
    else:
        q=input()
        to_and_fro(s,q)
