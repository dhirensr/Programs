def hourglass_row(row_no,arr):
    x=[]
    for i in range(4):
        x.append(arr[row_no][i]+arr[row_no][i+1]+arr[row_no][i+2]+\
        arr[row_no+1][i+1]+arr[row_no+2][i]+arr[row_no+2][i+1]+\
        arr[row_no+2][i+2])
    return x
arr=[[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
z=-999999
for i in range(4):
    y=hourglass_row(i,arr)
    if(max(y)>z):
        z=max(y)
print(z)
