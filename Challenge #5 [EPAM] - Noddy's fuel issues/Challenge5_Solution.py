from itertools import combinations
t=int(input())
for _ in range(t):
    fa=list(map(int,input().split()))[1:]#fa stands for fuel available
    tf=int(input())#tf stnds for target fuel
    mfl=int(input())#mfl stands for max fuel limit at aone station
    lenf=len(fa)
    sb=[]
    dfa=sorted(fa)
    lend=len(dfa)
    jsb=100
    for i in range(lend):
        if dfa[i]>mfl:
            dfa=dfa[:i]
            break
    for i in range(1,lenf):
        sb.extend(list(combinations(dfa,i)))
    for ele in sb:
        if sum(list(ele))==tf:
            jsb=10
            break
    if jsb==10:
        print('Yes')
    else:
        print('No')
    


