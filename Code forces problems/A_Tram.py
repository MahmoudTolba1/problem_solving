capac = []
counter = 0
for i in range(int(input())):
    exit,enter = map(int, input().split())
    
    counter += (enter - exit)
    capac.append(counter)
print(max(capac))
    