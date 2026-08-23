def last_occurance(arr,key):
    low = 0
    high = len(arr)-1
    ans = len(arr)
    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] == key:
            ans = mid
            low = mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return ans

arr = [1,3,5,7,8,9,9]
print(last_occurance(arr,9))