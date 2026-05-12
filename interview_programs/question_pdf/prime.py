# check whether gifen number is prime or not

# def prime(num):
#     flag = True
#     for i in range(2,int(num)):
#         if (num % i == 0):
#             flag = False
#     if flag:
#         print(f"{num} is prime number")
#     else:
#         print(f"num is not a prime number. ")

# prime(5)

# def sec_lrg_prime(arr):
#     primes = []
#     for num in arr:
#         if num < 2:
#             continue
#         is_prime = True
#         for i in range(2, int(num**0.5)+1):
#             if (num % i == 0):
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     primes = sorted(set(primes),reverse=True)
#     print(f" second largest prime num is - {primes[1]} ")
# sec_lrg_prime([2,3,7,5,8])


# without using lists

def sec_lrg_prime(arr):
    largest = -1
    sec_largest = -1
    for num in arr:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5+1)):
            if (num % i == 0):
                is_prime = False
                break
        if is_prime:
            if num > largest:
                sec_largest = largest
                largest = num
            elif num > sec_largest and num != largest:
                sec_largest = num
    if sec_largest != -1:
        print(f"second largest number is - {sec_largest}")
sec_lrg_prime([2,3,7,6,8])