def n_steps(x,y):
    r=0
    if x==y or x==y+2:
        if(x%2==0):
            r=x+y
        else:
            r=x+y-1
    else:
        return "No Number"
    return r

t=input()
for i in range(int(t)):
    x,y= input().split()
    print(n_steps(int(x),int(y)))
