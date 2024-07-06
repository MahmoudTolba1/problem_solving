tests = int(input())
for test in range(tests):
    x1,y1,x2,y2 = map(int,input().split())
    y = 0 
    y2 = -y2
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print(f"{d:.10f}")