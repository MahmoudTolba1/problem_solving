n, k = map(int, input().split())


for i in range(k):
    if n >= 0:
        n = str(n)
        if n[-1] != "0":
            n = int(n)
            n -= 1
        else:
            n = int(n)
            n //= 10
print(n)
         