def binary_search(arr,x):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = high - 1
    return -1

arr = [2,4,5,7,8,9,10,11]
print(binary_search(arr,10))