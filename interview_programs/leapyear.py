# y = 2000
# if(y % 4 == 0):
#     if y% 100 == 0:
#         if y % 400 == 0:
#             print("Leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")

# def is_leap_year(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 == 0:
#         return True
#     else:
#         False
# print(is_leap_year(2000))
def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
year = int(input("enter the year"))
print(is_leap_year(year))