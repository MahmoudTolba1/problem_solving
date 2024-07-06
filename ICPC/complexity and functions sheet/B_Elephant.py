# x = int(input())
# moves = [1,2,3,4,5]
# counter = 0

# while x > 0:
#     for i in range(1,len(moves)+1):
#         if x >= moves[-i]: 
#             x -= moves[-1]
#             counter += 1
# print(counter)

# lower complexity code
x = int(input())
counter = 0
while x != 0:
    if x >= 5:
        f = x // 5
        x -= 5 * f
        counter += f
    elif x >= 4 :
        f = x // 4
        x -= 4 * f
        counter += f
    elif x >= 3 :
        f = x // 3
        x -= 3 * f
        counter += f
    elif x >= 2 :
        f = x // 2
        x -= 2 * f
        counter += f
    else:
        f = x // 1
        x -= 1 * f
        counter += f
print(counter)