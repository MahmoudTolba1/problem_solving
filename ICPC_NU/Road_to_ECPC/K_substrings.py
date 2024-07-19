s  = input()

result1 = s.replace('AB', 'x',1)
result2=s.replace('BA','x',1)

if ('AB' in result2 and "BA" in s) or 'BA' in result1 and 'AB' in s:
    print("YES")
else:
    print("NO")