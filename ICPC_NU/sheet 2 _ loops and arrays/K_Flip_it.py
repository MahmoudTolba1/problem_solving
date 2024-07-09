n = int(input())
cubes = list(map(int,input().split()))

cubes.sort()
print(*cubes)

# for cube in range(len(cubes) - 1):
#     if cubes[cube] > cubes[cube + 1]:
#         cubes[cube + 1], cubes[cube] =  cubes[cube], cubes[cube + 1]
#     print(*cubes)