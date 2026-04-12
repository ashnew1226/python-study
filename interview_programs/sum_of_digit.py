def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    print(f"sum of given integer is : {total}")
num = int(input("enter the number : "))
sum_of_digits(num)