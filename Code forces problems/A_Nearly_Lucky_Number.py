string = input()
counter = 0

for i in string:
    if i == "4" or i == "7":
        counter += 1
if counter == 4 or counter == 7:
    print("YES")
else:
    print("NO")