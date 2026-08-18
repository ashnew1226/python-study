# def insertion_sort(arr):
    
#     if len(arr) <= 1:
#         return arr
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr

# arr = [64,25,12,22,11]
# print(insertion_sort(arr))


def insertion_sort(arr,n):
    if n <= 1:
        return
    insertion_sort(arr,n-1)
    key = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

arr = [64,25,12,22,11]
insertion_sort(arr,len(arr))
print(arr)