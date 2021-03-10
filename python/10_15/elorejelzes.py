N = int(input())
elorejelzes = []

for i in range(N):
    elorejelzes.append(input())
nap = 0

for x in elorejelzes:
    min = int(x.split()[0])

    if min < 0:
        nap += 1
print(nap)
