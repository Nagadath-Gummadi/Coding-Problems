def stepscount(l1,i,j,c):

    c1,c2,c3=999999999,999999999,999999999

    if(i==j==n-1):

        return c

    if(i!=n-1 and l1[i+1][j]==0):

        c1=stepscount(l1,i+1,j,c+1)

    if(j!=n-1 and l1[i][j+1]==0):

        c2=stepscount(l1,i,j+1,c+1)

    if(i==j and l1[i+1][j+1]==0):

        c3=stepscount(l1,i+1,j+1,c+1)

    return min(c1,c2,c3)

t=int(input())

while(t>0):

    n,n=map(int,input().split())

    l1=[]

    for i in range(n):

        l1.append(list(map(int,input().split())))

    print(stepscount(l1,0,0,0))

    t-=1
