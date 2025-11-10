
def binary_search(arr,target):
    low = 0
    highest = len(arr) - 1
    while low <= highest:
        mid = (low + highest)// 2
        print(f"---{mid}")
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
            print(f"low - {low}")
        else:
            highest = mid - 1
            print(f"high - {highest }")

    return -1
nums = [1, 3, 5, 7, 9, 11, 13]
result = binary_search(nums, 9)
print(result)