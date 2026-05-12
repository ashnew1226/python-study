# Bruth force approach
# n = [5,9,6,2,8,1]
# for i in range(len(n)-1):
#     for j in range(len(n)-i-1):
#         print(f"- {len(n)-i-1}")
#         if n[j] > n[j+1]:
#             n[j],n[j+1] = n[j+1],n[j]
# print(n)

# optimized o(n) time complexity
# def bubble(arr):
#     n = len(arr)
#     for i in range(n-1):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1],arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     print("sorted elements : ",arr)
# arr = [64, 25, 12, 22, 11]     
# bubble(arr)

def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    print(arr)
bubble([23,21,7,26,6])