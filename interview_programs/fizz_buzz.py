def fizz_buzz(num):
    total = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
print(fizz_buzz(16))