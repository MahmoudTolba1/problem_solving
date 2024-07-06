input = input()
names = set()

for i in range(len(input)):
    names.add(input[i])
if len(names) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")