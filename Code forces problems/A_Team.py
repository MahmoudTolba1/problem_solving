# cont, suma = [] , []
# counter = summ = 0
# for _ in range(int(input())):
#     cont[_] = list(map(int,input().split()))
#     # for i in cont:
#     #     for j in range(len(i)):
#     #         i[j] = int(i[j])
# # for x in cont:
# #     for r in range(len(x)):
# #         summ += x[r]
# #         suma.append(summ)
    

# print(cont)
# # print(suma)
# # print(counter)
# ################################################################

# lista = []
# for _ in range(int(input())):
#     lista.append(input().split())
#     for i in lista:
#         for j in range(len(i)):
#             i[j] = int(i[j])

# suma = []

# for i in lista:
#     suma.append(sum(i))
# counter = 0
# for i in suma:
#     if i > 1:
#         counter += 1
# print(counter)

count = 0
for _ in range(int(input())):
    row = list(map(int, input().split()))
    if sum(row) > 1:
        count += 1
print(count)