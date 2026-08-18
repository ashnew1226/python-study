# s = "Ashish"
# # print(s[::-1])
# new_s = ""

# for i in s:
#     new_s = i + new_s
# print(new_s)

# s = "ashish"
# freq = {}
# for char in s:
#     freq[char] = freq.get(char,0)+1
# print(freq)

# x = 10
# def test():
#     global x # Till here value of x will be 10 as declared globally

#     x = 20  # from here it is changed
#     print(x)
# test()
# print(x)


# def fibo(n):
#     if n <= 1:
#         return n

#     return fibo(n-1) + fibo(n-2)
# for i in range(7):
#     print(fibo(i))

# numbers = [1,2,3,4]
# result = list(map(lambda x:x*x, numbers))
# print(result)

# Static method
# dont need class data, dont need object data 
# class Math:
#     @staticmethod
#     def add(a,b):
#         return a+b
# m = Math()
# print(m.add(10,20))
# print(Math.add(10,20))


# Class methods

# class Employee:
#     company_name = "BMW"
#     @classmethod
#     def change_name(cls,name):
#         cls.company_name = name
#         print(cls.company_name)
# e = Employee()
# e.change_name("Google")


# Exception handeling
# try:
#     value = int(input("Enter the number : "))
#     result = 10/value
#     print(result)
# except ValueError as e:
#     print("Error : ",e)
# except ZeroDivisionError as a:
#     print("Error: ",a)


# Custom excetion handeling

# class InsufficientBalanceError(Exception):
#     pass
# def withdraw(amount,balance):
#     if amount > balance:
#         raise InsufficientBalanceError("amount is greater than balance")
#     return balance - amount
# try:
#     balance = withdraw(1500,1000)
#     print(balance)

# except InsufficientBalanceError as e:
#     print("Transaction failed:",e)



# class InsufficientBalance(Exception):
#     pass

# try:
#     amount = 1500
#     balance = 1000
#     if amount > balance:
#         raise InsufficientBalance("insufficient balance : ")

# except InsufficientBalance as e:
#     print("Amount Error : ",e)

# finally:
#     print("Program completed")



