n = int(input())
lista = list(map(int,input().split()))
lista2 = [0] * n
for index, value in enumerate(lista):
    index += 1
    value -= 1
    lista2[value] = index
print (*lista2)


# for i in range(len(lista)):
#     lista2[lista[i] - 1] = i+1
# print(*lista2)