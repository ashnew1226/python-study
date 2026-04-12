# def fibo(n):
#     a,b = 0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b = b, a + b
#     return a
# print(fibo(10))

def fibocheck(n):
    a,b = 0,1
    even = 0
    isfibo = False
    while a <= n:
        if a == n:
            isfibo = True
        if a % 2 == 0:
            even += a
        a, b = b, a + b

    if isfibo and n > 1:
        print(n)
    else:
        print(even)
fibocheck(16)