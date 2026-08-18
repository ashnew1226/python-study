def quick_sort(arr,low,high):
    if low < high:
        p = partition(arr,low,high)

        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)


def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low+1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
        else: 
            break
    arr[low],arr[j] = arr[j],arr[low]
    return j


arr = [64,25,12,22,11]
quick_sort(arr,0,len(arr)-1)
print(arr)