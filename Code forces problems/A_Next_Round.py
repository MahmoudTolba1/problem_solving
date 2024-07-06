
n, k = map(int, input().split())
lista = list(map(int, input().split()))
count = 0
for i in range(n):
    if lista[i] >= lista[k - 1] and lista[i] > 0:
        count += 1
print(count)


# n, k = map(int, input().split())

# for _ in range(n):
#     input_values = input().split()
#     lista = []
#     for value in input_values:
#         lista.append(int(value))
#     count = 0
#     for i in range(len(lista) - 1):
#         if lista[i] >= lista[i + 1] and count <= k and lista[i] != 0:
#             count += 1
#     print(count)

# n,k=[int(i)for i in input().split()]
# a=sorted([int(i)for i in input().split()],reverse=True)
# cnt=0
# for i in range(n):
#     if a[i]>0 and a[i]>=a[k-1]:
#         cnt+=1
# print(cnt)