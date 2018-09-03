t = int(input().strip())
m = [int(i) for i in input().strip().split()]
n = [int(j) for j in input().strip().split()]
one_array=[]
two_array=[]
three_array=[]
for i in range(t):
    if n[i]==1:
        one_array.append(m[i])
    elif n[i]==2:
        two_array.append(m[i])
    else:
        three_array.append(m[i])


min_one=min(one_array) if one_array else 0
min_two=min(two_array) if two_array else 0
min_three=min(three_array) if three_array else 0
if min_one==0 and min_two ==0:
    print(min_three)
elif min_one + min_two > min_three and min_three!=0:
    print(min_three)
elif min_three==0:
    print(min_one + min_two)
