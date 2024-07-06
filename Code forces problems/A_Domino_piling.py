# M ,N = map(int,input().split())
# perimeter = M * N
# dominoes = perimeter // 2
# print(dominoes)



# M, N = map(int, input().split())
# print((M * N) // 2)



print((lambda M, N: (M * N) // 2)(*map(int, input().split())))