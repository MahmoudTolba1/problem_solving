n = int(input())
lista = list(map(int, input().split()))
lista.sort()
div = 0
for i in lista:
    if i != 0:
        div += i / max(lista)

out = div*max(lista) / n

print(f"{out:.12f}")