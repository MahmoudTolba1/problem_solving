s =input()
seta = set()
for i in range(len(s)):
    if s[i].isalpha():
        seta.add(s[i])
print(len(seta))
