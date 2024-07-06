x, y = map(int,input().split())
counter = 0
for i in range(x+1):
    for j in range(y+1):
        if i*j == i:
            counter += 1
print(counter)