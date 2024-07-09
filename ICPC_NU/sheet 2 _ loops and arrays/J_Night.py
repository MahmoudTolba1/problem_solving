n = int(input())
stw = list(map(int, input().split()))

if n < 3:
    print(0)
else:
    min_strength = min(stw)
    max_strength = max(stw)
    
    if min_strength == max_strength:
        print(0)
    else:
        counter = 0
        for strength in stw:
            if min_strength < strength < max_strength:
                counter += 1
        print(counter)