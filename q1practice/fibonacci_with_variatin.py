# def fibonacci(i):
#     if i <= 1:
#         return i
#     else:
#         return fibonacci(i-1) + fibonacci(i-2)
# terms = int(input(" enter the number of terms : "))
# for i in range(0,terms+1):
#     print(fibonacci(i),end=" ")
# print()


# 1 to n number using recursion\
def num_return(n):
    if n == 0:
        return 0
    return n + num_return(n-1)
n = int(input("enter the number : "))
res = num_return(n)
print("res = ",res)