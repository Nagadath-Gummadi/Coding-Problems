n=int(input())
raw=[]
for i in range(n):
    seq=input()
    raw=seq.split(" ") 
    i=1
    dim=int(raw[0])
    j=1
    fend=[]
    while(i<=dim):
        fend.append((dim*(dim-i))+j)
        i=i+2
        j=j+1
    i=0
    j=0
    bend=[]
    while(i<(dim-1)):
        bend.append((dim*(dim-i))-j)
        i=i+2
        j=j+1
    bend.reverse()
    fend.extend(bend)
    for i in fend:
        print(chr(((int(raw[i+1]))%26)+96),end="")
    print()
