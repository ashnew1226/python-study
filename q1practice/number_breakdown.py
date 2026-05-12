# This is by using string and math

# def num_breakdown(num):
#     num_str = str(num)
#     n = len(num_str)
#     parts = []
#     for i in range(n):
#         digit = int(num_str[i])
#         if digit != 0:
#             value = digit * (10 ** (n - i - 1))
#             parts.append(str(value))
#     print("+".join(parts))
# num_breakdown(12345)

#  By using math
# def num_breakdown(num):
#     place = 1
#     result = []
#     while num > 0:
#         digit = num % 10
#         if digit != 0:
#             result.append(str(digit*place))
#         num //= 10
#         place *= 10
#     print("+".join(result[::-1]))
# num_breakdown(12345)