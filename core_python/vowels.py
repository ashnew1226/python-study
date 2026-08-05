# s = input("enter the string.")
# vowels = "aeiouAEIOU"
# count = 0

# for i in s:
#     if i in vowels:
#         count += 1
# print(count)

# Factorial

# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(4))
    

# fibonacci

# a = 0
# b = 1
# for _ in range(10):
#     print(a)
#     a,b = b, a+b


# Duplicate elements in array

# arr = [1,2,3,2,4,4]
# seen = set()
# dup = set()

# for i in arr:
#     if i in seen:
#         dup.add(i)
#     seen.add(i)
# print(dup)

# iterators
numbers = [10,20,30]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))