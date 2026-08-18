def check_ele(arr,n):
    ele = False
    for i in range(len(arr)):
        if arr[i] == n:
            ele = True
            break
    if ele:
        print(f"index of {n} : {i} ")
    else:
        print(f"element {n} is not present in array")

arr = [2,1,4,6,3]
check_ele(arr,5)