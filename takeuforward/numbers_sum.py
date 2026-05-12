def numbers_sum(num):
    result = 0
    while num > 0:
        digit = num % 10
        result += digit
        num = num//10
    print(result)
numbers_sum(100000001)