num = int(input())
lista = ["I hate that I love", "that", "it"]
if num == 1:
    print("I hate it")
elif num == 2:
    print(f"{lista[0]} " + lista[2])
elif num % 2 == 0 and num > 2:
    print(f"{lista[0]} "* (num -1) + lista[2])


# if num % 2 == 0 and num > 1:
#     print(f"{lista[0]} {lista[3]} {lista[1]} {lista[2]} " * (num - 1))

# else:
#     print(f"{lista[0]} {lista[3]} {lista[1]} {lista[3]} {lista[0]}" * (num -2) + f" {lista[2]}")