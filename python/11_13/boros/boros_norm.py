N= int(input())
halmaz=set()

for _ in range(N):
    akt=input().split()
    halmaz.add(int(akt[1]))

print(len(halmaz))