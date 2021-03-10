# print(len(set([int(input().split(" ")[1]) for _ in range(int(input()))])))

N=int(input())
halmaz=set()

for _ in range(N):
    akt=input().split()
    halmaz.add(akt[1])

print(len(halmaz))
