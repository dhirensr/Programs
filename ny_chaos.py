def NewYearChaos(queue):
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False

    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            return "Too chaotic"
    # bubble sorting to find the answer
    for i in range(0, lastIndex):
        for j in range(0, lastIndex):
            if queue[j] > queue[j+1]:
                queue[j],queue[j+1] = queue[j+1],queue[j]
                swaps += 1
                swaped = True

        if swaped:
            swaped = False
        else:
            break
    return swaps

print(NewYearChaos([2,5,1,3,4]))
