# year = int(input())
# year += 1
# year = str(year)

# check = True
# while check == True:
#     lista = []
#     for i in year:
#         if i not in lista:
#             lista.append(i)
#     if len(lista) <=3:
#         year = int(year)
#         year += 1
#         year = str(year)
#     else:
#         check = False
# print(year)

s = int(input()) + 1
while len(set(str(s))) < 4:
    s += 1
print(s)
