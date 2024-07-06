n = int(input())
output = 0


lista = list(map(int,input().split()))
output += len(lista)
for i in range(len(lista)):
    icount = 0
    if lista.count(lista[i]) > 1:
        output += 1
        for j in lista:
            if j  == lista[i]:
                lista[i] = " "
print(output)
