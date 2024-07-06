string1, string2, string3 = input(), input(), input()
lista = []
if len(string3) == len(string1+string2):
    for i in string3:
        if  i in string1+string2 and string3.count(i) == (string1+string2).count(i):
            lista.append("YES")
        else:
            lista.append("NO")
    if "NO" in lista:
        print("NO")
    else:
        print("YES")       
else:
    print("NO")