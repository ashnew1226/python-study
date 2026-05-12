# def palindrome(num):
#     original = num
#     reversed = 0
#     while num > 0:
#         digit = num % 10
#         reversed = reversed * 10 + digit
#         num = num // 10
#     if original == reversed:
#         print("palindrome")
#     else:
#         print("not palindrome")
# palindrome(121)


text = input("enter the string.")

if text == text[::-1]:
    print("palindrome")
else:
    print("not palindrome")