# def print_name(n,name):
#     if n == 0:
#         return
#     print(name)
#     print_name(n-1,name)

# print_name(3,"ashish")

def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1)+fibo(num-2)
num = int(input("Enter n : "))
print(f"number at position {num} is - {fibo(num-1)}")
print(f"fibo till {num} are :")
for i in range(num):
    print(fibo(i),end=" ")