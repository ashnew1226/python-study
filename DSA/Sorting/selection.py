# arr = [78,3,5,5,56,1,4]
# print("Before Sort - ")
# print(arr)
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1,len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i],arr[min_index] = arr[min_index], arr[i]
# print("After Sort - ")
# print(arr)



# def selection_sort(arr):
    # n = len(arr)
    # for i in range(n):
    #     min_index = i
        # for j in range(i + 1,n):
            # if arr[j] < arr[min_index]:
            #     min_index = j
    #     # arr[i], arr[min_index] = arr[min_index], arr[i]
    # print(arr)

# arr = [3,2,7,1,9]
# selection_sort(arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    print(arr)

selection_sort([23,12,6,5,3,9])