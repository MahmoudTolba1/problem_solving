n = input()
counter = 1
lista = list(map(int,input().split()))
lista.sort(reverse = True)
v = lista[0]
for i in range(len(lista) - 1):
    if v <= sum(lista[i+1:]):
        counter += 1
        v += lista[i+1]
print(counter)