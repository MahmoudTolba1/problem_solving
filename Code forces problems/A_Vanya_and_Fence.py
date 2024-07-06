nfrnd, fhight = map(int, input().split())
H = list(map(int, input().split()))
counter = 0
for i in range(nfrnd):
    if H[i] <= fhight:
        counter += 1
    else:
        counter += 2
print(counter)