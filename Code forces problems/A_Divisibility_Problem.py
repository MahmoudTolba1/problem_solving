for i in range(int(input())):
    a, b = map(int, input().split())
    counter = 0

    if a %b == 0:
        print(0)
    else:
        print(abs((a % b) - b))