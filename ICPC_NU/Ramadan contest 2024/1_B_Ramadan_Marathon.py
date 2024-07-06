teams, place = map(int, input().split())
rank = []
for i in range(teams):
    problems,time = map(int, input().split())
    rank.append([problems,-time])
rank.sort(reverse=True)

result = rank.count(rank[place-1])

print(result)