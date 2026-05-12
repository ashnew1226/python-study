# def find_start_time(s,t):
#     sh,sm = map(int,s.split(":"))
#     th,tm = map(int,t.split(":"))
#     sm -= tm
#     if sm < 0:
#         sm += 60
#         sh -= 1
#     sh -= th
#     if sh < 0:
#         sh += 24
#     print(f"{sh:02d}:{sm:02d}")
# find_start_time("06:30","06:20")


# def power_of_4(arr):
#     for num in arr:
#         if num > 0 and (num & (num -1) == 0) and (num & (0x55555555)) != 0:
#             print(num)
# power_of_4([2, 16, 8, 12, 64])

# binary maximum possible odd number 
# def max_possible_odd(bnum):
#     zeros = "" 
#     ones = ""
#     for s in bnum:
#         if s == '1':
#             ones += '1'
#         elif s == '0':
#             zeros += '0'
#     print("".join(ones[:-1])+zeros+'1')

# max_possible_odd("01010110")

# Time given current time 's' time spend 't' findout start time

# def start_time(s,t):
#     sh,sm = map(int,s.split(":"))
#     th,tm = map(int,t.split(":"))
#     sm -= tm
#     if sm < 0:
#         sm += 60
#         sh -= 1
#     sh -= th
#     if sh < 0:
#         sh += 24
#     print(f"{sh:02d}:{sm:02d}")
# start_time("0:00","1:00")


# rearrange letters if not palindrome return letters if not return -1
# def rearrange_letters(s):
#     if len(s) == 1:
#         return -1
#     rev = s[::-1]
#     if rev == s:
#         return -1
#     arr = list(s)
#     arr[-1],arr[-2] = arr[-2],arr[-1]
#     return "".join(arr)
# print(rearrange_letters("abccba"))

# excrypted pattern

# def encrypted_pattern(s):
#     return (s[2]+s[3]+s[1]+s[4]+s[0])
# print(encrypted_pattern("rmgae"))

