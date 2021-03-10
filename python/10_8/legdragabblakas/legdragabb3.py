# Egy ingatlanforgalmazó cégtárolja az eladó lakások alapterületét és árát.
# Írj programot,amely megadja alegdrágább lakás sorszámát!

# Harmadik megoldás:
# Kigyűjtjük listába, és használjuk a python beépített függvényeit

N = int(input())
teruletek, arak = [], []
for _ in range(N):
    a = input().split()
    arak.append(int(a[1]))
    # a területek lista felesleges(elhagyható)
    teruletek.append(int(a[0]))

# max(arak) megadja a lista legnagyobb értékű elemét
# az arak.index() megadja az adott elem hanyadik helyen van a listában
legdragabb = arak.index(max(arak)) + 1

print(legdragabb)
