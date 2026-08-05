# def is_leap(year):
#     return (year % 100 == 0 or year % 400 != 0) and (year % 4 == 0 )

# year = int(input("enter the year : "))
# print(is_leap(year))

# def is_prime(num):
#     if num <= 1:
#         return False
#     else :
#         for i in range(2,int(num**0.5) + 1):
#             if (num % i == 0):
#                 print(f"{num} is not prime number")
#                 return
#             else:
#                 print(f"{num} is a prime number")
#                 return
# num = int(input("Enter the number : "))
# is_prime(num)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

arr = [3,1,7,9,2,5]
bubble_sort(arr)

