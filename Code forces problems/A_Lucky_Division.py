n = input()

def is_lucky(n):
    n = str(n)
    for i in n:
        if i not in ["4", "7"]:
            return False
    else:
        return True

n = int(n)

for i in range(1, n + 1):
    if n % i == 0 and  is_lucky(i):
        print("YES")
        break
else:
    print("NO")


# n = int(input())

# lista = []
# for i in range (1, 1000000):
#     i = str(i)
#     for j in i:
#         if j not in ["4", "7"]:
#             break
#     else:
#         lista.append(int(i))

# for _ in lista:
#     if n % _ == 0:
#         print("YES")
#         break
# else:
#     print("NO")