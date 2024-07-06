for _ in range(int(input())):
    counter = 0
    a , b , c = map(int,input().split())
    counter += a
    if b > 3 and c > 3:
        if b % 3 == 1 and c % 3 == 0:
            counter += b // 3
            counter += c // 3
        # elif b % 3 != 0 and c % 3 != 0:

    else:
        counter += 1
        counter += 1

    print(counter)