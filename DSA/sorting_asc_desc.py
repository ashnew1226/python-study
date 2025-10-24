# n = [2,7,3,9,1]
# for i in range(len(n)-1):
#     print(n[i])
#     for j in range(len(n)-i-1):
#         print(f"-----{n[j]}")
#         if n[j] > n[j+1]:
#             n[j],n[j+1] = n[j+1],n[j]
# print(n)
# n = [2,7,3,9,1]
# for i in range(len(n)-1,0,-1):
#     print(n[i])
#     for j in range(i):
#         print(f"-----{n[j]}")
#         if n[j] > n[j+1]:
#             n[j],n[j+1] = n[j+1],n[j]
# print(n)




# n = [2,7,3,9,1]
# for i in range(len(n)-1):
#     print(n[i])
#     for j in range(len(n)-i-1):
#         print(f"-----{n[j]}")
#         if n[j] < n[j+1]:
#             n[j],n[j+1] = n[j+1],n[j]
# print(n)


# finding lowest element in array
# a = [6,4,8,3,9,2]
# low = a[0]
# for i in a:
#     if i < low:
#         low = i
# print(low)