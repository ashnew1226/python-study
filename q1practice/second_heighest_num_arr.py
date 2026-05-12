def second_heighest(arr):
    first = float("-inf")
    second = float("-inf")
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second
print(second_heighest([3, 5, 7, 1, 10, 14, 6]))