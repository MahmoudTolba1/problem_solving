counter = 1
lista = []
for i in range(int(input())):
    lista.append(int(input()))
for i in range(len(lista) -1):
    if lista[i] != lista[i + 1]:
        counter += 1
print(counter)