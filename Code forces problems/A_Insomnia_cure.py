k, l, m, n, d = int(input()), int(input()), int(input()), int(input()), int(input())
dmg_drgns = 0

for i in range(1,d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        dmg_drgns += 1

print(dmg_drgns)