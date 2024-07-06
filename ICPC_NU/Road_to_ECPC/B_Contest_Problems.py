from collections import Counter

for i in range(int(input())):
    lista = Counter()
    xx=int(input())
    for j in range(xx):
        s, e = map(int,input().split())
        ls=[_ for _ in range(s,e+1)]
        lista.update(ls)
    if lista.most_common()[0][1]== xx:
        print('YES')
    else:
        print('NO')