import math
n = int(input())
for _ in range (n):
    a,b,c = map(int,input().split())
    d=int(b/a)
    if d>c:
        print (0)
    else:
        print (c-d)