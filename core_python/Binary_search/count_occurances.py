
def first_occurance(arr,x):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            mid = ans
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans


def last_occurance(arr,x):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            mid = ans
            low = mid + 1
        elif arr[mid] < x:
            low = mid - 1
        else:
            high = mid + 1
    return ans


