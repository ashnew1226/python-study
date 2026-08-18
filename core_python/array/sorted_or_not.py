def sort_or_not(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            print("array is not sorted")
            return
sort_or_not([46,25,12,22,11])