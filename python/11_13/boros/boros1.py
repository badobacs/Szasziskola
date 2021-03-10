N= int(input())
arak=[]
counter=0
for _ in range(N):
    ar=int((input().split())[1])
    if ar not in arak:
        counter +=1
    arak.append(ar)
print(counter)

