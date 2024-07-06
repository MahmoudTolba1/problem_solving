cost , dollars , bananas = map(int, input().split())
total_cost = 0 
for i in range(1,bananas+1):
    total_cost += cost * i
needed = total_cost - dollars

if needed >= 1:
    print(needed)
else:
    print(0)