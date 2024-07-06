string = input()
greet = ['h','e','l','l','o']
counter = 0

for i in string:
    if i == greet[counter]:
        counter += 1
        if counter == 5:
            print('YES')
            break
else:
    print("NO")