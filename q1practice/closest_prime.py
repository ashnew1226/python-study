# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2,int(num ** 0.5)+1):
#         if num % i == 0:
#             return False
#     return True
# def closest_prime(num):
#     d = 1
#     while True:
#         upper = num + d
#         lower = num - d
#         lowest_prime = is_prime(lower) if lower > 1 else False
#         upper_prime = is_prime(upper)
#         if lowest_prime and upper_prime:
#             print(f"closest prime numbers are {upper},{lower}")
#             return
#         elif lowest_prime:
#             print(f"closest prime number is {lower}")
#             return
#         elif upper_prime:
#             print(f"closest prime number is {upper}")
#             return
#         d += 1
    
# closest_prime(19)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def closest_prime(num):
    d = 1
    while True:
        lower = num - d 
        upper = num + d 
        lower_prime = is_prime(lower) if num > 1 else False
        upper_prime = is_prime(upper)
        if lower_prime and upper_prime:
            print(upper,lower)
            return
        elif lower_prime:
            print(lower)
            return
        elif upper_prime:
            print(upper)
            return
        d += 1
closest_prime(30)


