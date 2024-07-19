n = int(input())
lista = list(map(int, input().split()))

min_value = min(lista)
max_value = max(lista)

max_index = lista.index(max_value)

min_index = len(lista) - 1 - lista[::-1].index(min_value)

max_to_first = max_index

min_to_last = n - 1 - min_index

if max_index > min_index:
    steps = max_to_first + min_to_last - 1
else:
    steps = max_to_first + min_to_last

print(steps)
