# def armstrong_num(num):
#     temp = num
#     digits = len(str(num))
#     sum_power = 0
#     while temp > 0:
#         digit = temp % 10
#         sum_power += digit ** digits
#         temp //= 10
#     if num == sum_power:
#         print("armstrong")
#     else:
#         print("not armstrong")
# armstrong_num(173)


# def armstrong_range(start,end):
#     for num in range(start,end+1):
#         temp = num
#         digits = len(str(num))
#         sum_power = 0
#         while temp > 0:
#             digit = temp % 10
#             sum_power += digit ** digits
#             temp //= 10
#         if sum_power == num:
#             print(num,end=" ")
# armstrong_range(10,1000)
# num  = int(input("enter the number : "))

# for i in range(1,int(num**0.5)+1):
#     if num % i == 0:
#         print(i, end=" ")


# faster version to print all divisors
# num = int(input("Enter a number: "))

# for i in range(1, int(num**0.5) + 1):
#     if num % i == 0:
#         print(i,end=" ")
#         if i != num // i:
#             print(num // i,end=" ")

# check prime number :


def is_prime(num):
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            print("not prime.")
    print(num,"is prime number")

is_prime(17)