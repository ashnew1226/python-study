def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    print(arr)

arr = [1,0,2,3,0,4]
move_zeros(arr)