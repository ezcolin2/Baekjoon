import sys
input = sys.stdin.readline
def ccw(x1, y1, x2, y2, x3, y3):
    return  x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
a=ccw(x1, y1, x2, y2, x3, y3)
b=ccw(x1, y1, x2, y2, x4, y4)
c=ccw(x3, y3, x4, y4, x1, y1)
d=ccw(x3, y3, x4, y4, x2, y2)
print(1 if a*b<0 and c*d<0 else 0)