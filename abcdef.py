def abcdef(n):
    elements=[]
    A=[]
    B=[]
    ans=0
    for i in range(n):
        elements.append(int(input()))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                z=(elements[a]*elements[b])+elements[c]
                A.append(z)
                if(elements[c]!=0):
                    z=(elements[a]+elements[b])*elements[c]
                    B.append(z)
    A.sort()
    B.sort()
    for i in set(A):
        ans+=(A.count(i) * B.count(i))
    print(ans)

n=input()
abcdef(int(n))
