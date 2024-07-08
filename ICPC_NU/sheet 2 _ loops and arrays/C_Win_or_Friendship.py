n, string = int(input()), input()
Ac, Dc = 0,0
for i in range(n):
    if string[i] == "A":
        Ac += 1
    else:
        Dc += 1
if Ac > Dc:
    print("Anton")
elif Dc > Ac:
    print("Danik")
else:
    print("Friendship")


# string = input()[1:]  # Read the entire input and slice from the second character
# Ac, Dc = string.count('A'), string.count('D')

# print("Anton" if Ac > Dc else "Danik" if Dc > Ac else "Friendship")