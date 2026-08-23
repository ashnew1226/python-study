def floor_ceil(arr, x):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] == x:
            return arr[mid], arr[mid]
        if arr[mid] < x:
            floor = arr[mid]
            low = mid + 1
        else:
            ceil = arr[mid]
            high = mid - 1
    return floor,ceil

arr = [1,3,5,6,7,8,9]
print(floor_ceil(arr,4))
