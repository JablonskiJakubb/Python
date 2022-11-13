# zad 1
# for i in range (1, 31):
#     print(i, end=" ")

# zad 2
# for i in range (1, 100, 2):
#     print(i**2, end=" ")

# zad 3
# for i in range (1000,10001):
#     if i % 379 == 0:
#         print(i, end=" ")

# # zad 4
# for i in range (100,999):
#     if i%5 == 0 or i%6 ==0 or i%11 == 0:
#         print (i, end=" ")

# zad 5

# suma = 0
# a = int(input("ile liczb"))
# for i in range(0,a):
#     n = int(input("podaj liczbę"))
#     suma = suma+n
#     if i == a-1:
#         print(suma,end=" ")

# zad 6
# n = int(input("ile liczb poczatkowych: "))
# suma = 0
# for i in range(0,n*2, 2):
#     suma = suma + i
#     if i == n*2 - 2:
#         print(suma)

# zad 7

# n = int(input("Ile liczb poczatkowych: "))
# suma = 0
# for i in range(11, 10 + ((n*2) + 1), 2):
#  suma = suma + i
# if i == 10 + n*2 - 1:
#    print(suma)

# zad 8
# suma = 0
# w = int(input("Kwota wejściowa: "))
# l = int(input("Okres inwestycji: "))
# suma = w
# for i in range(1, l*12):
#     a = suma*0.06*(1/12)
#     suma = suma + a
# print(suma)

# zad 9
# suma = 0
# n = int(input("ile liczb początkowych"))
# for i in range (21,n*100,100):
#     suma = suma + i
# print(suma)

# zad 10
# import math
# for i in range(1, 1000):
#     if i%10 == math.sqrt(i):
#         print(i)
#     if i%100 == math.sqrt(i):
#         print(i)

