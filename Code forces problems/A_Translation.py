# be, bi = input(), input()
# output = ""

# for i in range(len(be)):
#     if be[i] == bi[-(i+1)]:
#         output = "YES"
#     else:
#         output = "NO"
# print(output)

x= input()
 
y= input()
conter=0
s=len(y)-1
for i in x:
    if i == y[s]:
 
        conter+=1
        s+=-1
    else:
        break
if conter==len(y):
    print("YES")
else:
    print("NO")