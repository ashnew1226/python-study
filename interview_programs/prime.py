    # def prime_num(num):
    #     flag = False
    #     if num == 0 or num == 1:
    #         print("not a prime number")
    #     elif(num>1):
    #         for i in range(2,num):
    #             if (num % i) == 0:
    #                 flag = True
    #                 break
    #         if flag:
    #             print(f"{num} is not a prime number")
    #         else:
    #             print(f"{num} is prime number ")
    # num = int(input("enter the number"))
    # prime_num(num)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): # || it is used for checking few iteration instead of each iteration 
        # print("n--",n)
        # print("i--",i)
        if n % i == 0:
            return False
    return True
def closest_prime(num):
    d = 1
    while True:
        lower = num-d 
        upper = num+d
        lower_prime = is_prime(lower) if lower > 1 else False
        upper_prime = is_prime(upper) 
        if lower_prime and upper_prime:
            print(f"lower_prime - {lower} upper_prime - {upper}")
            return
        elif lower_prime:
            print(f"lower_prime - {lower}")
            return
        elif upper_prime:
            print(f"upper_prime - {upper}")
            return
        d += 1 
num = int(input("enter the number : "))
closest_prime(num)