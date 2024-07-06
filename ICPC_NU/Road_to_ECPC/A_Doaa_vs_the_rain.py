N, H, W = map(int, input().split())
for i in range(N):
    sH, sW = input().split()
    sgw =  sbh = "" 
    if sH == "Y":
        H -= 1
        W += 1
        sgw = "Y"

    elif sH == "N" and W == 0:
        H -= 1
        W += 1
        sgw = "Y"
    
    else:
        sgw = "N"
    
    if sW == "N" and H == 0:
        W -= 1
        H += 1
        sbh = "Y"
    
    elif sW == "N" and H != 0:
        sbh = "N"
        
    else:
        W -= 1
        H += 1
        sbh = "Y"
    print(f"{sgw} {sbh}")