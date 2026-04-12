def count_power_of_two(arr):
    count = 0
    for num in arr:
        if num > 0 and (num & (num-1))==0:
            count += 1
    return count
print(count_power_of_two([1, 0, 4, 9, 6, 16]))