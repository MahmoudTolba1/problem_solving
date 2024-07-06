import math
n = int(input())
lista = list(map(int,input().split()))
sumlista = sum(lista)
sumn = (n*(n+1)) // 2
missing = sumn - sumlista

print(math.floor((abs(missing - sumlista/(n-1)))))