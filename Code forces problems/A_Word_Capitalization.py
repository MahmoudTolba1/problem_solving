input = input()
lista = []
for i in range(len(input)):
    lista.append(input[i])
lista[0] = lista[0].upper()
print(''.join(lista))