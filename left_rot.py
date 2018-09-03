def rot_left(arr,d):
    rotation_elements=arr[:d]
    other_elements=arr[d:]
    result=other_elements+rotation_elements
    return result

print(rot_left([1,2,3,4,5],2))
