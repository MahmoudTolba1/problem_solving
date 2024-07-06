for i in range(int(input())):
    word = ()
    lista = []
    s = input()
    if len(s) == 1:
        print("NO")
    elif len(s) > 1:
        for i in s:
            lista.append(i)
            s2 = set(lista)
        if len(s2) == 1:
            print("NO")
        else:
            s3 = lista[0]
            print(f"YES\n{s[1:]+s3}")
