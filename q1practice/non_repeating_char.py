# def non_repeating_char(s):
#     freq = {}
#     for char in s:
#         freq[char] = freq.get(char,0)+1
#     for char in s:
#         if freq[char] == 1:
#             print(f"non repeating char is : {char}")
#             return
# s = input("enter the string : ")
# non_repeating_char(s)

# sum of digit

# def digit_sum(num):
#     while num >= 10:
#         result = 0
#         while num > 0:
#             digit = num % 10
#             result += digit
#             num //= 10
#         num = result
#     return result
# num = int(input("enter the number : "))
# print(digit_sum(num))


# def non_repeat_char(word):
#     freq = {}
#     for char in word:
#         freq[char] = freq.get(char,0)+1
#     for char in word:
#         if freq[char] == 1:
#             print(f"non repeating char is : {char}") 
#             return
# non_repeat_char("amazom")

def sum_of_digit(num):
    result = 0
    while num > 0:
        digit = num % 10
        result += digit
        num //= 10
    return result
print(sum_of_digit(8483))


def sum_of_digit(num): # till single digit
    while num >= 10:    
        result = 0
        while num > 0:
            digit = num % 10
            result += digit
            num //= 10
        num = result
    return result
print(sum_of_digit(8483))