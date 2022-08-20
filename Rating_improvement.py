t=int(input())
for i in range(t):
    x,y=[int(x) for x in input().split()]
    #z=x<=x+200
    if x<y<x+200:
       print("YES")
    else:
       print("NO")
