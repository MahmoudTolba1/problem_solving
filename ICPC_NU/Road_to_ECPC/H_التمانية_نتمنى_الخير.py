n = int(input())
lista = input().split()
output = ""

for i in range(1,n+1):
    if lista[i-1] == str(i) or lista[i-1] == "mumble":
        output += "makes sense"
    else:
        output += "something is fishy"
if "something is fishy" in output:
    print("something is fishy")
else:
    print("makes sense")