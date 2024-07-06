import random
n = int(input())
lista = []
rn = random.randint(1, 100)
counter = 1
for i in range(n):
    if rn + counter % rn != 0:
        lista.append(rn + counter)
        counter += 1
print(*lista)
