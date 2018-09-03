def ap_or_gp(n_list):
    next_element=0
    if(n_list[1]-n_list[0] == n_list[2]-n_list[1]):
        d=n_list[1]-n_list[0]
        next_element = n_list[-1] + d
        print('AP',next_element)
    else:
        d=n_list[1] // n_list[0]
        next_element = int(n_list[-1] * d)
        print('GP',next_element)


i=0
while(i!=-1):
    a=[int(i) for i in input().split()]
    if(a[0]==a[1] == a[2]==0):
        i=-1
    else:
        ap_or_gp(a)
