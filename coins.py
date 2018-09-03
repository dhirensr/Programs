values={}
values[0]=0
values[1]=1
def coins(n):
    if n in values:
        return values[n]
    else:
        values[n] = max(n,coins(n/2)+coins(n/3)+ coins(n/4))
        return values[n]

try:
    while True:
        n = int(input())
        print(coins(n))
except:
    pass
