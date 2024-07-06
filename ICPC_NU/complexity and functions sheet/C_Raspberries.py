
# def prod(li):
#     p = 1
#     for i in li:
#         p *= i
#     return p

# for i in range(int(input())):
#     n,k = map(int,input().split())
#     lista = []
#     for i in range(n):
#         lista.append(map(int,input().split()))
#     counter = 0
    
    
#     if prod(lista) % k == 0:
#         print(counter)
#     else:
#         for i in lista:
            

#             counter += 1
#             if prod(lista) % k == 0:
#                 print(counter)
#                 break

t = int(input())
INF = 10000000000
for i in range(t):
    f = 0
    n,k = map(int,input().split())
    ar = [int(i) for i in input().split()]
    mind = INF
    for x in range(len(ar)):
        if ar[x] % k == 0:
            f = 1
            mind = 0
            break
        if ar[x] > k:
            mind = min(mind,k-(ar[x]%k))
        else:
            mind = min(mind,k - ar[x])
    if k == 4 and f == 0:
        q = 0
        for x in range(len(ar)):
            if ar[x] % 2 == 0:
                q += 1
        if q >= 2:
            mind = 0
        else:
            mind = min(mind, 2 - q)
    print(mind)