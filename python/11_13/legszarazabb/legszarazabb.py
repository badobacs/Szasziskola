N=int(input())
hetek=[]
for i in range(N):
    x=int().split(" ")
    for i in range(len(x)):
        x[i]=int(x[i])
    hetek.append(sum(x))

index=0
minimum=hetek[0]+hetek[1]
for i in range(len(hetek)-1):
    osszeg=hetek[i]+hetek[i+1]
    if osszeg<minimum:
        minimum=osszeg
        index=i

print(index+1)
