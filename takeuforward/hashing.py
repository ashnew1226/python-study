# # Manual hashing 
# arr = list(map(int,input(" enter the numbers : ").split()))
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# for key,value in freq.items():
#     print(key,"->",value)





# # # Manual hashing find a maximum count element in array
# arr = list(map(int,input(" enter the numbers : ").split()))
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# max_count = 0
# max_element = 0
# for key,value in freq.items():
#     # print(key,"->",value)
#     if value > max_count:
#         max_count = value
#         max_element = key
# print("maximum count element is : ",max_element)
# print("maximum count frequency is : ",max_count)