counter = 0
for i in range(int(input())):
    people, maxcapacity = map(int, input().split())
    if people <= (maxcapacity - 2):
        counter += 1
print(counter)