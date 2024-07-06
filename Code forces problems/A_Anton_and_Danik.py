n, string = input(), input()
counter  = 0

for i in string:
    if i == "A":
        counter +=1
    else:
        counter -= 1
if counter > 0:
    print('Anton')
elif counter < 0:
    print('Danik')
else:
    print('Friendship')