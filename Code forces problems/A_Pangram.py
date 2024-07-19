n = int(input())
string = input().lower()
set = set()

for i in range(n):
    set.add(string[i])

if len(set) == 26:
    print("YES")
else:
    print("NO")