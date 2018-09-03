def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    return arr
def min_swaps(arr):
    num=arr.copy()
    swaps=0
    count=0
    num.sort()
    for i in range(len(arr)):
        if(arr[i]!=num[i]):
            swap(arr,i,arr.index(num[i]))
            count+=1
    return count

print(min_swaps([1,3,5,2,4,6,8]))
