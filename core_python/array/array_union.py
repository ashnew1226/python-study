def arr_union(arr1,arr2):
    new_arr = []
    for i in arr1:
        if i not in new_arr:
            new_arr.append(i)
    for j in arr2:
        if j not in new_arr:
            new_arr.append(j)
    print(new_arr)
arr_union([1,2,2,4,5,],[4,5,6,6,7])
