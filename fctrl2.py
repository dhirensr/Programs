facts=[1]*101
def fctrl2(n):
    if(n==1):
        return 1
    elif(facts[n]!=1):
        return facts[n]
    elif (facts[n-1]!=1):
        return n* facts[n-1]
    else:
        for i in range(1,n+1):
            facts[i]= i * facts[i-1]
        return facts[n]

t=input()
for j in range(int(t)):
    n=input()
    print(fctrl2(int(n)))
