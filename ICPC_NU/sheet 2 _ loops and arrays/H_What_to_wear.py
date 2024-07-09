# n = int(input())
# teams = []
# matches_list = []
# counter = 0
# matches = n * (n-1)

# for i in range(n):
#     x, y = map(int, input().split())
#     teams.append([x, y])

# # make a list that contains all the matches
# for team in range(len(teams)):
#     for opponent_team in range(len(teams)):
#         if team != opponent_team:
#             matches_list.append([teams[team], teams[opponent_team]])

# for match in range(matches - 1):
#     if matches_list[match][0][0] == matches_list[match][1][1]:
#         counter += 1
# print(counter)


n = int(input())
teams = []

for _ in range(n):
    h, a = map(int, input().split())
    teams.append((h, a))

counter = 0

for i in range(n):
    for j in range(n):
        if i != j:
            if teams[i][0] == teams[j][1]:
                counter += 1

print(counter)