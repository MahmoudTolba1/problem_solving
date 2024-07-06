# lista = []
# for _ in range(int(input())):
#     line = input().split()
#     lista.extend(list(map(int, line)))
# if sum(lista) == 0:
#     print("YES")
# else:
#     print("NO")

x=y=z = 0

for _ in range(int(input())):
    lista = list(map(int, input().split()))
    x += lista[0]
    y += lista[1]
    z += lista[2]
if x != 0 or y != 0 or z != 0:
    print("NO")
else:
    print("YES")