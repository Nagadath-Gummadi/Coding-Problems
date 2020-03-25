import math
t=int(input())
for i in range(t):
    a=list(map(int,input().strip().split()))
    n=a[0]
    a.pop(0)
    for i in range(n):
        if a[i]==-1:
            if abs(a[i-1]-a[i+1])%2==0:
                a[i]=abs(a[i-1]-a[i+1])
            else:
                a[i]=math.floor((a[i-1]+a[i+1])/2)
    for i in range(n):
        if a[i]!=1 and i!=n-1:
            a[i]=a[i]-1;
        print(a[i],end="")
    print()
