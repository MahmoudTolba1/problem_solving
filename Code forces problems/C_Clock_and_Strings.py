lista = [1,2,3,4,5,6,7,8,9,10,11,12]
for _ in range(int(input())):
    lista2 = []
    lista3 = []
    a,b,c,d = map(int,input().split())
    lista2 = lista[min(a,b)-1 : max(a,b)]
    for i in lista:
        if i not in lista2:
            lista3.append(i)
    if c in lista2 and d not in lista2 or c not in lista2 and d in lista2:
        print("YES")
    else:
        print("NO")