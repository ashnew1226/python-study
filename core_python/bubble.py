def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

bubble_sort([7,2,5,1,3,9])