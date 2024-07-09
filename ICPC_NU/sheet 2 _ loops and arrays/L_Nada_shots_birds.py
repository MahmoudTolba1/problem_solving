

# n = int(input())
# birds = list(map(int, input().split()))
# m = int(input())
# updated_bird_list = []

# for _ in range(m):
#     wire, bird = map(int, input().split())
#     for i 


n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    xi, yi = map(int, input().split())
    wire = xi - 1 
    pos = yi

    if wire > 0:
        a[wire - 1] += pos - 1
    if wire < n - 1:
        a[wire + 1] += a[wire] - pos

    a[wire] = 0

for birds in a:
    print(birds)