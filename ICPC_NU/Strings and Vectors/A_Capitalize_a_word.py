# input = input()
# lista = []
# for i in range(len(input)):
#     lista.append(input[i])
# lista[0] = lista[0].upper()
# print(''.join(lista))

string = input()

first_char = string[0]
first_char = first_char.upper()
print(first_char + string[1:])