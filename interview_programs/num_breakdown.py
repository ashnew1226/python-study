# def number_breakdown(num):
#     s = str(num)
#     length = len(s)
#     parts = []
#     for i in range(length):
#         digit = int(s[i])
#         if digit != 0:
#             value = (digit * (10 ** (length - i - 1)))
#         parts.append(str(value))
#     print("+".join(parts))
# num = int(input("enter the number : "))
# number_breakdown(num)

def number_breakdown(n):
    if n == 0:
        print(0)
        return
    place = 1
    parts = []
    while n > 0:
        digit = n % 10
        if digit != 0:
            parts.append(str(digit*place))
        n //= 10
        place *= 10
    print(" + ".join(parts[::-1]))
number_breakdown(10500)