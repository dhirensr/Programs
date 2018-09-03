t = int(input().strip())
series = [i * (i+1)//2 for i in range(1, 44725)]

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = (lower + upper) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break
            lower = x
        elif target < val:
            upper = x
    return lower

for i in range(t):
    loss = 0
    x= input()
    if int(x) in series:
        loss=series.index(int(x))+1
        print(loss)
    else:
        nearest_element = binary_search(series, int(x))
        if (abs(series[nearest_element] - int(x)) > abs(series[nearest_element+1] - int(x))):
            nearest_element+=1
        dist= abs(int(x) - series[nearest_element])
        loss= dist+nearest_element+1
        print(loss)
