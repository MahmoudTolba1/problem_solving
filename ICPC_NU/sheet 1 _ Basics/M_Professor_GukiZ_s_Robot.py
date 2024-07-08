x1, y1= map(int,input().split())
x2, y2= map(int,input().split())

xdiff = abs(x1 - x2)
ydiff = abs(y1 - y2)
print(max(xdiff , ydiff))