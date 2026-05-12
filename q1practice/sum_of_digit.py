def sum_of_digit(num):
    while num >= 10:            # used for result till single digit 
        total = 0
        while num > 0:
            digit = num % 10
            total += digit
            num = num // 10
        num = total
    print(f"sum of integer is : {total}")
num = int(input(" enter the number : "))
sum_of_digit(num)