def sort_binary_array(arr):
    left = 0   # used left pointer to place the next 0 occurence
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i],arr[left] = arr[left],arr[i]
            left += 1
    return arr
print(sort_binary_array([1,0,1,0,1,0,1,0]))