N, T = map(int,input().split())
a = b = c = d = T
listac = []
listaf = []
listap = []
listaq = []
for i in range(N):
    place, time_to = input().split()
    if place == "C":
        listac.append(int(time_to))
    elif place == "F":
        listaf.append(int(time_to))
    elif place == "P":
        listap.append(int(time_to))
    else:
        listaq.append(int(time_to))
listac.sort()
listaf.sort()
listap.sort()
listaq.sort()
counter = 0
for i in listac:
    if a >= i:
        a -= i
        counter += 1
for i in listaf:
    if b >= i:
        b -= i
        counter += 1
for i in listap:
    if c >= i:
        c -= i
        counter += 1
for i in listaq:
    if d >= i:
        d -= i
        counter += 1
print(counter)