input = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u','y']

for i in input:
    if i in vowels:
        input = input.replace(i,'')

input = '.' +'.'.join(input)
print(input)