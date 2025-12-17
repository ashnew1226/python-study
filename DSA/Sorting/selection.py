arr = [78,3,5,5,56,1,4]
print("Before Sort - ")
print(arr)
for i in range(len(arr)):
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index], arr[i]
print("After Sort - ")
print(arr)
