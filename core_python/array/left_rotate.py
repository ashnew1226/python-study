def left_rotate(arr):
    first = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = first
    return arr
arr = [64,25,12,22,11]
print(left_rotate(arr))