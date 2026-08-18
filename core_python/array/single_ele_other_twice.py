def single_ele(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
print(single_ele([1,1,2,2,5,3,5]))