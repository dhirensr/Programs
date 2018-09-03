import math,sys,time
# naive approach
def check_prime(a):
    flag=1
    if(a==1):
        flag=0
        return 0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            flag=0
            break
    return flag

#print(check_prime(1))
#Segmented Sieve of Eratosthenes
def calculate_prime(a,b):
    j=0
    sqrt=int(math.sqrt(b))
    array=[1 for i in range(sqrt+1)]
    primes=[-999 for u in range(sqrt+1)]
    for i in range(2,sqrt+1):
        k=i+i
        if(array[i]==1):
            primes[j]=i
            j+=1
            while(k<=sqrt): #make multiples as not prime
                array[k]=0
                k+=i
    diff=(b-a)+1
    array=[1 for i in range(diff)]
    for k in range(j):
        div= int(a/primes[k])
        div*=primes[k]
        while(div<=b):
            if(div>=a and primes[k]!=div):
                array[div-a]=0
            div+=primes[k]
    for i in range(diff):
        if(array[i]==1 and (i+a)!=1):
            print(i+a)
    return 0

t=input()
for j in range(int(t)):
    x,y=input().split()
    start_time = time.time()
    calculate_prime(int(x),int(y))
    if(j!=(int(t)-1)):
        print()
    print("--- %s seconds ---" % (time.time() - start_time))
