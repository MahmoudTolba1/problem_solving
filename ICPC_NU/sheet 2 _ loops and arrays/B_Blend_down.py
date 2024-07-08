numOfFriends, wallHight= map(int, input().split())
hightList = list(map(int, input().split()))

minimumWidth = 0

for i in hightList:
    if i <= wallHight:
        minimumWidth += 1
    else:
        minimumWidth += 2
print(minimumWidth)