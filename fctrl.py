#https://brilliant.org/wiki/trailing-number-of-zeros/
def fctrl(n):
    i=0
    counter=0
    if(n>4):
        while(n > (5** i)):
            i+=1
            counter+= int(n / (5**i))
    print(counter)

t=input()

for i in range(int(t)):
    a=input()
    fctrl(int(a))
