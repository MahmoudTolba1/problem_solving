t = int(input())

n = []
for i in range(t):
    n.append(int(input()))

myString = "AA"
myString2 = "BAA"
for i in n:
    if i % 2 != 0:
        print("NO")
    else:
        print("YES")
        if i == 2:
            print(myString)
        else:
            mystring3 = myString2 * (i//2)
            print(mystring3)