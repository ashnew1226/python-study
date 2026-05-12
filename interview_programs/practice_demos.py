# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# def closest_prime(num):
#     d = 1
#     while True:
#         lower = num - d
#         upper = num + d
#         lowest_prime = is_prime(lower) if lower > 1 else False
#         upper_prime = is_prime(upper)
#         if lowest_prime and upper_prime:
#             print(f"closest prime numbers are - {lower},{upper}")
#             return
#         elif lowest_prime:
#             print(f"closest prime number - {lower}")
#             return
#         elif upper_prime:
#             print(f"closest prime number - {upper}")
#             return
#         d += 1
# num = int(input("enter the number : "))
# closest_prime(num)

# def non_rep_char(str):
#     freq = {}
#     for char in str:
#         if char in freq:
#             freq[char] += 1
#         else:
#             freq[char] = 1
#     for char in str:
#         if freq[char] == 1:
#             print(f"non repeated char is : {char}")
#             return
# str = input("enter the string : ")
# non_rep_char(str.lower())

# def sum_digit(num,single_digit = False):
#     total = 0
#     while num > 0:   
#         digit = num % 10
#         total += digit
#         num = num // 10
#     if single_digit:
#         while total >= 10:  # repeat until single digit
#             temp = 0
#             while total > 0:
#                 digit = total % 10
#                 temp += digit
#                 total = total // 10
#             total = temp 

#     return total
# num = int(input(" enter the number : "))
# print(sum_digit(num))
# print(sum_digit(num,True))

# def is_power_of_four(n):
#     if n <= 0:
#         return False
#     # Check power of 2 and additional condition for power of 4
#     print(f"n --- {n}")
#     print(f"n-1 --- {n-1}")
#     print(f"(n-1) % 3 --- {(n-1) % 3}")
#     return (n - 1) % 3 == 0


# def print_power_of_four(arr):
#     result = []
#     for num in arr:
#         if is_power_of_four(num):
#             result.append(num)
#     print(*result)


# # Example
# arr = [2, 16, 8, 12, 64]
# print_power_of_four(arr)

# def sec_smallest(arr):
#     first = second = float("inf")
#     for num in arr:
#         if num < first:
#             second = first
#             first = num
#         elif num < second and num != first:
#             second = num
#     return second
# print(sec_smallest([3,5,10,14,6]))

# def num_breakdown(num):
#     place = 1
#     parts = []
#     while num > 0:
#         digit = num % 10
#         if digit != 0:
#             parts.append(str(digit * place))
#         num //= 10
#         place *= 10
#     print(" + ".join(parts[::-1]))

# num_breakdown(10500)

# def is_leap(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# def next_leap(year, n):
#     result = []
#     year += 1
#     while year % 4 != 0:
#         year += 1
#     while len(result) < n:
#         if is_leap(year):
#             result.append(str(year))    
#         year += 4
#     print(", ".join(result))
# next_leap(999,1)


# Decode string problem 

# def decode_string(s):
#     stack = []
#     for char in s:
#         if char != "]":
#             stack.append(char)
#         else:
#             current_str = ""
#             while stack and stack[-1] != "[":
#                 current_str = stack.pop() + current_str
#             stack.pop()
#             num = ""
#             while stack and stack[-1].isdigit():
#                 num = stack.pop() + num
#             stack.append(current_str *int(num))
#     return "".join(stack)
# print(decode_string("3[a]2[bc]"))    # accaccacc



#max odd binary from given binary

# def max_odd_binary(s):
#     ones = ''
#     zeros = ''
#     for n in s:
#         if n == '1':
#             ones += '1'
#         elif n == '0':
#             zeros += '0'
#     print(ones[:-1] + zeros + '1')
# max_odd_binary("01010110")
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             print(f"i = {i}")
#             return False
#     return True

# print(is_prime(18))
# def closest_primary(num):
#     d = 1
#     while True:
#         lower = num - d 
#         upper = num + d
#         lower_prime = is_prime(lower) if lower > 1 else False
#         upper_prime = is_prime(upper)
#         if lower_prime and upper_prime:
#             print(lower,upper)    
#             return
#         if lower_prime:
#             print(lower)
#             return
#         if upper_prime:
#             print(upper)
#         d+=1
# closest_primary(30)
