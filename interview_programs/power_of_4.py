# def power_of_4(arr):
#     for n in arr:
#         if n > 0 and (n & (n-1)) == 0 and (n & 0x55555555) != 0:
#             print(n)
# power_of_4([2, 16, 8, 12, 64])

def is_power_of_4(arr):
    result = []
    for num in arr:
        n = num
        while n > 1:
            if n % 4 != 0:
                break
            n //= 4
        if n == 1:
            result.append(num)
    print(result)
is_power_of_4([2, 16, 8, 12, 64])