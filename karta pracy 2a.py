import math
# # zad 1
#
# a = int(input())
# b = int(input())
#
# if (a+b)%2==0:
#     print("TAK")
# else:
#     print("NIE")

# zad 2
# a = int(input())
# g = int(input())
#
# if (a + g)/2> math.sqrt(a*g):
#     print("arytmetyczna większa")
# else:
#     print("geometryczna większa")

# zad 3
# k = int(input())
# l = int(input())
# m = int(input())

# if (k==l and m!=k and m!=l):
#     print ("TAK równe są ", k, "i", l)
# else:
#     if (k == m and l != m and k != l):
#         print("Tak równe są", k, "i", m)
#     else:
#         if (m == l and k != m and k != l):
#             print("Tak równe są", m, "i", l)
#         else:
#             if (k != l and l != m and k != m):
#                 print("żadna nie jest równa")
#
# k = int(input())
# l = int(input())
# m = int(input())
#
# if (k == l and m != k and m != l):
#     print("TAK równe są ", k, "i", l)
# else:
#     if (k != l and m == k and m != l):
#         print("TAK, równe są ", m, "i", k)
#     else:
#         if (k != l and m != k and m == l):
#             print("TAK, równe są ", m, "i", l)
#         else:
#             print("NIE, żadna z nich nie jest równa lub wszystkie 3 są równe")
#
# zad 4
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# print("najmniejsza z nich to")
# if (a < b and a < c and a < d):
#     print(a)
#
# if (a > b and c > b and b < d):
#     print(b)
#
# if (c < b and d > c and a > c):
#     print(c)
#
# if (d < b and d < c and a < d):
#     print(d)

# zad 5
# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b > c and a + c > b and b + c > a):
#     print("spełnia")
# else:
#     print("nie spełnia")

# # zad 6
# a = int(input())
# b = int(input())
# c = int(input())
# if (a+b+c==180):
#     print("trójkąt")
# else:
#     quit("nie jest trójkątem")
# if (a or b or c > 90):
#     print("rorwartokątny")
# elif (a or b or c == 90):
#     print("prostokątny")
# elif (a and b and c > 90):
#     print("ostrokątny")

