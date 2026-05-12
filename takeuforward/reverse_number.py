def reverse_num(num):
    result = ""
    while num > 0:
        digit = num % 10
        result += str(digit)
        num = num //10
    print(result)
reverse_num(123)