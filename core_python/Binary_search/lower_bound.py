def lower_bound(arr,x):
    low = 0
    high = len(arr)-1
    ans = len(arr)

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [1,3,4,4,6,8,9,10]
print(lower_bound(arr,4))