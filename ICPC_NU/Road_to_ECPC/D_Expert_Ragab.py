for _ in range(int(input())):
    keyboard, string = input(),input()
    pos = []
    for i in string:
        for j in range(len(keyboard)):
            if i == keyboard[j]:
                pos.append(j)
    sum = 0   
    if len(pos) == 1 or len(set(pos)) == 1:
        print(0)
        continue
    else:
        for s in range(len(pos)-1):
            sum += abs(pos[s] - pos[s+1])  
    print(sum)