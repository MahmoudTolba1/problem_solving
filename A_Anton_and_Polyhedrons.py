
n = int(input())
lista = []
poly = {"Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20}
result = 0
for _ in range(n):
    lista.append(input())

for i in lista:
    if i in poly:
        result += poly[i]
print(result)