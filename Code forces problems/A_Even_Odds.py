# n, k = map(int, input().split())
# listao = []
# listae = []
# for i in range(1,n+1):
#     if i % 2 == 0:
#         listae.append(i)
#     else:
#         listao.append(i)
# lista = listao + listae
# print(lista[k-1])


num,c=map(int,input().split())
half=(num/2)
ceiled_result = int(half) + (half % 1 > 0)
if c>ceiled_result:
    res=int((c-ceiled_result)*2)
else:
    res=int((c*2)-1)
print (res)