# for _ in range(int(input())):
#     a,b,c=map(int,input().split())
#     if b*2 <= c :
#         print(a*b)
#     else:
#         f=a//2
#         s=f*2
#         print((f*c)+((a-s)*b))

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(a * b if b * 2 <= c else (a // 2 * c) + ((a - a//2 * 2)*b))
