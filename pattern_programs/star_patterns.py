# num = int(input("enter the number of rows"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# output : 
# enter the number of rows5
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


# num = int(input("enter the number of rows"))
# k = 1
# for i in range(1,num+1):
#     for j in range(1,k+1):
#         print("*", end=" ")
#     k = k+2
#     print()

# output : 
# enter the number of rows3
# * 
# * * * 
# * * * * * 


# num =int(input("enter the number of rows"))
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print()

# output : 
# enter the number of rows5
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# n = 5
# for i in range(n,0,-1):          # colums
#     for j in range(n-i):
#         print(end=" ")      # Print Spaces
#     for j in range(i):
#         print("*",end=" ")  # Print stars
#     print("")

# output : 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# n = 5
# for i in range(n):
#     print(" "*(n-i-1)+("* "*(i+1)))
# output : 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

# n = 5 
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()
# n = 5
# for i in range(n,0,-1):
#         print("*"*i)
    

# *****
# ****
# ***
# **
# *
# n = 5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()

# def pyramid(rows):
#     for i in range(rows):
#         print(" "*(rows-i-1)+"* "*(i+1))
#     for j in range(rows):
#         print(" "*(j+1)+"* "*(rows-j-1))

# pyramid(5)

# output : 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
n = 5 
# for i in range(n):
#     print(" "*(n-i)+"*"*(i+1))
# output : 
#      *
#     **
#    ***
#   ****
#  *****

# for i in range(n):
#     print(" "*(i+1)+"*"*(n-i))
# output :
#  *****
#   ****
#    ***
#     **
#      *

# n = int(input("enter number of rows"))

# for row in range(n):
#     for col in range(n-row):
#         print("*",end="")
#     for col in range(row*2+1):
#         print(" ",end="")
#     for col in range(n-row):
#         print("*",end="")
#     print()

# for row in range(n):
#     for col in range(row+1):
#         print("*",end="")
#     for col in range((2 * n - 1) - 2 * row):
#         print(" ",end="")
#     for row in range(row+1):
#         print("*",end="")
#     print()

# output : 
# enter number of rows5
# ***** *****
# ****   ****
# ***     ***
# **       **
# *         *
# *         *
# **       **
# ***     ***
# ****   ****
# ***** *****

# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end="")
#     print()
# output :
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# output :
# 1
# 12
# 123
# 1234
# 12345

# for i in range(n+1,1,-1):
#     for j in range(1,i):
#         print(j,end="")
#     print()

# output : 
# 12345
# 1234
# 123
# 12
# 1

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if ((i+j) % 2 == 0):
#             print("1",end="")
#         else:
#             print("0",end="")
#     print()
# output :
# 1
# 01
# 101
# 0101
# 10101
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+j),end="")
#     print()
# A
# AB
# ABC
# ABCD
# ABCDE