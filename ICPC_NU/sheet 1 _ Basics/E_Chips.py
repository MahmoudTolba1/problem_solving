# n , m = map(int, input().split())
# check = True
# for i in range(1, n+1):
#     if m < i+1:
#         check = False
#         break
#     m -= i
# if check == True:
#     print(m-1)
# else:
#     print(m)

n , m = map(int, input().split())

m %= (n * (n+1) // 2)
for i in range(1, n+1):
    if m < i:
        break
    else:
        m -= i
print(m)