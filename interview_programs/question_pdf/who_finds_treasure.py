# # 
# def who_finds_treasure(a, x, y):
#     print(type(a))
#     target = a + 0.5
#     total = 0
#     turn = 1

#     while True:
#         if turn == 1:
#             total += x
#             if total >= target:   # ✅ fix
#                 return "First"
#             turn = 2
#         else:
#             total += y
#             if total >= target:   # ✅ fix
#                 return "Second"
#             turn = 1


# print(who_finds_treasure(1, 2, 4))
# print(who_finds_treasure(2, 1, 4))
# print(who_finds_treasure(2, 2, 1))

# simple math approach
def who_finds_treasure(a, x, y):
    target = 2 * a + 1
    cycles = 2*(x+y)
    k = target // cycles
    total = k * cycles
    remaining = target - total
    if remaining <= 2 * x:
        return "First"
    return "Second"
# examples
print(who_finds_treasure(1, 2, 4))  # Second
print(who_finds_treasure(2, 1, 4))  # Second
print(who_finds_treasure(2, 2, 1))  # First