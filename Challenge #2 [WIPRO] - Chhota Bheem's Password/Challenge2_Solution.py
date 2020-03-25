n=int(input())
passwd=[]
for i in range(n):
    hint=input()
    raw=(hint.split(" "))
    for i in range(int(raw[0])):
        if((raw[i])=='-1'):
            if(int(raw[i-1])%2==0 and int(raw[i+1])%2==0):
                raw[i]=abs(int(raw[i-1])-int(raw[i+1]))
            elif(int(raw[i-1])%2!=0 and int(raw[i+1])%2!=0):
                raw[i]=abs(int(raw[i-1])-int(raw[i+1]))
            else:
                raw[i]=int((int(raw[i-1])+int(raw[i+1]))/2)   
    for i in range(int(raw[0])):
        if(i!=0 and i!=len(raw) and int(raw[i])!=1):
            raw[i]=int(raw[i])-1
    for i in range(len(raw)):
        if(i==0):
            continue
        print(raw[i],end="")  
    print()
