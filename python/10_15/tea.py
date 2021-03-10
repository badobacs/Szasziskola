N = int(input())
fajtak = []
for _ in range(N):
    fajta = input()
    mennyiség = input()
    if fajta not in fajtak:
        fajtak.append(fajta)
print(len(fajtak))
