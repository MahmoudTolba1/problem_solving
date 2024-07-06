string1,string2, string3 = input(), input(), input()
string4 = string1 + string2
out =[]
lista1 = []
lista2 = []
if len(string3) == len(string4):
    for i in range(len(string4)):
        lista1.append(string4[i])
        lista2.append(string3[i])
    lista1.sort()
    lista2.sort()   
    if lista1 == lista2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")