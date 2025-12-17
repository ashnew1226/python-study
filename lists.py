fruits = ["banana","guava","kiwi","apple","grapes"]
# new_list = []
# for i in fruits:
#     if "a" in i:
#         new_list.append(i)

# new_list = [x.upper() for x in fruits]
# print(new_list)
# new_list = [x for x in fruits if "a" in fruits]
# print(fruits)
new_list = [x  if x != "banana" else "orange" for x in fruits]
print(fruits)