# def sum_of_multiplies(n):
#     total = 0
#     for i in range(n):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total
# print(sum_of_multiplies(10))


def sum_of_multiples(n):
    def sum_k(k):
        m = (n-1) // k
        print(f"k- {k}, m - {m}")
        sum = k*(m*(m+1)//2)
        print(sum)
        return sum
    return sum_k(3)+sum_k(5)-sum_k(15)
print(sum_of_multiples(10))