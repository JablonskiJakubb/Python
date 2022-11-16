# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j, end="\t")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     print()

# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for k in range(n-i-1, n):
#         print("*", end="")
#     print()
# n=4
# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     for k in range(n-i-1, n):
#         print("", end="")
#     print()

# zad 1
# n = int(input("ile chcesz tych śmiesznych znaczków"))
# if (n == 4):
#     print(" ")
#     print("ty jebany betoniarzu")
# else:
#     for i in range (n):
#         print("*-|", end="")


# # zad 2
# n = int(input())
# for i in range(1,n+1):
#     print("*"*i, end="")
#     if i % 2:
#         print("||", end="")
#     else:
#         print("--", end="")
# print()

# n = int(input())
# for i in range(1,n+1):
#     print("*"*i, end="")
#     if i%2:
#         print("||", end="")
#     else:
#         print("--", end="")

# zad 3
# n = int(input())
# for i in range(1,n+1):
#     print("*", end="")
#     if i % 2 == 1:
#         print("|"*i, end="")
#     else:
#         print("-"*i, end="")

# zad 4
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i + j == 2 or i+j ==6 or i ==3 and j == 1 or j == 3 and i == 1 :
#             print("*", end="")
#         else:
#             print("-", end="")
#     print()


# zad 5

# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j == n//2 + 1:
#             print("*", end="")
#         else:
#             print(" ", end=" ")
#     print()

# zad 6
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print("*", end="")
#         elif i+j==n-1:
#             print("?", end="")
#         else:
#             print("-", end="")
#     print()
    #       1      2      3      4      5
    # 1 (1, 1) (1, 2) (1,*3) (1, 4) (1, 5)
    # 2 (2, 1) (2, 2) (2, 3) (2, 4) (2, 5)
    # 3 (3,*1) (3, 2) (3, 3) (3, 4) (3, 5)
    # 4 (4, 1) (4, 2) (4, 3) (4, 4) (4, 5)
    # 5 (5, 1) (5, 2) (5, 3) (5, 4) (5, 5)

    #      1      2      3      4      5
    #1 (1, 1) (1, 2) (1, 3) (1, 4) (1, 5)
    #2 (2, 1) (2, 2) (2, 3) (2, 4) (2, 5)
    #3 (3, 1) (3, 2) (3, 3) (3, 4) (3, 5)
    #4 (4, 1) (4, 2) (4, 3) (4, 4) (4, 5)
    #5 (5, 1) (5, 2) (5, 3) (5, 4) (5, 5)

# # zad 7
# n = int(input())
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or j == 1 or i == n or j == n or (i == n//2 + 1 and j == n//2 + 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

for i in range (1,11):
    for j in range(1,11):
        print("({i},{j})",end=" ")
    print()
