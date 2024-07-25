n, m = int(input()), int(input())

def fastPower(x,n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * x
        x = x*x
        n = n // 2

    return result

# we want to calculate m mod 2**n
if n <= 40:
    print(m % fastPower(2, n))
else:
    print(m)