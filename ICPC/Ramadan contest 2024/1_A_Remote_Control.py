testcase = int(input())

counterlist = []
for i in range(testcase):
    a,b = map(int,input().split())

    counter = 0
    result = abs(a-b)
    while result != 0:
        if result >= 5:
            f = result // 5
            result -= 5 * f
            counter += f
        elif result >= 2 :
            f = result // 2
            result -= 2 * f
            counter += f
        else:
            f = result // 1
            result -= 1 * f
            counter += f
    counterlist.append(counter)

for i in counterlist:
    print(i)
