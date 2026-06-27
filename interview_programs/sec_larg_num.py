def sec_lrg_num(arr):
    first = float("-inf")
    second = float("-inf")
    for num in arr:
        if num > first:
            second = first
            print(f"first--{first}")
            print(f"second--{second}")
            print(f"num--{num}")
            print("------------------")
            first = num
        elif num > second and num != first:
            print("elif------------")
            print(f"second -- {second}")
            print(f"num -- {num}")
            second = num
    return second

         
print(sec_lrg_num([3, 5, 7, 1, 6, 14, 10]))   # 10

