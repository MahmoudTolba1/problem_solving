# players = input()
# sum = 0
# zcounter = []
# ocounter = []
# for i in range(len(players)-1):
#     if players[i] == players[i+1] == "1":
#         sum += 1
#         ocounter.append(sum)
#     elif players[i] == players[i+1] == "0":
#         sum += 1
#         zcounter.append(sum)
# for j in range(len(zcounter)):
#     if ocounter[j] >= 7 or zcounter[j] >= 7:
#         print("YES")
#         break
#     else:
#         print("NO")
#         break

string = input()
zstring = "0000000"
ostring = "1111111"

if zstring in string or ostring in string:
    print("YES")
else:
    print("NO")