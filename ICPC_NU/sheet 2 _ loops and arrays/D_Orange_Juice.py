# n, b, d = map(int, input().split())
# sizes = list(map(int, input().split()))
# counter = 0

# for i in range(n):
#     if sizes[i] < b:
#         listsum = sum(sizes)
#         counter = listsum//d
# print(counter)

n, b, d = map(int, input().split())
sizes = list(map(int, input().split()))

waste = 0
empties = 0

for size in sizes:
    if size <= b:
        waste += size
        if waste > d:
            empties += 1
            waste = 0

print(empties)