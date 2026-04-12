def equilib(arr):
    total_sum = sum(arr)
    left_sum = 0
    for num in arr:
        total_sum -= num
        if total_sum == left_sum:
            return num
        left_sum += num
    return 0 
print(equilib([1,7,5,6,2]))