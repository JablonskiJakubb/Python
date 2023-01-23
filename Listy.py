# for elem in L:
#     print(elem,end=",")
# print("\n")
#
# for i in range(len(L)):
#     print(L[i], end = ",")
# print("\n")
# //Wygeneruj tablicę n losowych liczb:
# from random import randint
# 
# L=[randint(1,20) for i in range (20)]
# print(f"Lista: {L}")
#
# print("maks")
# print(max(L))
# print("min")
# print(min(L))
# print("ilość max")
# print(L.count(max(L)))
# print("ilość min")
# print(L.count((min(L))))
# print("różnica miedzy max a min")
# print(max(L) - min(L))
# print("suma wartości")
# print(sum(L))
# print("średnia")
# print(sum(L)/len(L))
# print("ilość parzystych czy nieparzystych jest większa")
# x = 0
# for i in L:
#     if x%2==0:
#         x+=1
#     elif x%2!=0:
#         x-=1
# if x>0:
#     print("parzyste")
# else:
#     print("nieparzystych")
# print("v-ce maks i v-ce min")
# for i in range(L.count(max(L))):
#     L.pop(L.index(max(L)))
# print(max(L))
# for i in range(L.count(min(L))):
#     L.pop(L.index(min(L)))
# print(min(L))
# print("prostszy sposób")
# print(L)
# print(list(set(L)))
# S = list(set(L))
# print(S[len(S) - 2])

# print("ile pierwszych")
# 1. Znajdź największą liczbę w tablicy
# 2. Znajdź najmniejszą liczbę w tablicy
# 3. Podaj ile razy występuje najwieksza liczba w tablicy
# 4. Podaj ile razy występuje najmniejsza liczba w tablicy
# 5. Podaj rozpiętość tablicy (różnica max - min)
# 6. Podaj sumę liczb w tablicy
# 7. Podaj średnią wartość liczb w tablicy
# 8. Których liczb jest więcej w tablicy: parzystych czy nieparzystych?
# 9. Ile w tablicy jest liczb pierwszych?
# 10. Podaj v-ce max i v-ce min liczb tablicy
