# x = 0

# for i in range(int(input())):
#     inp = input()
#     if inp == "++X" or inp == "X++":
#         x += 1
#     else:
#         x -= 1
# print(x)

x = 0
for i in range(int(input())):
    user_input = input()
    if user_input in ["++X", "X++"]:
        x += 1
    else:
        x -= 1
print(x)

# x = sum(1 if input() in ["++X", "X++"] else -1 for _ in range(int(input())))
# print(x)