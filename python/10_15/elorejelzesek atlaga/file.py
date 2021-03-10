bemenet = open("be1.txt", "r")

bemenet_meretek = bemenet.readline().split()
N, M = int(bemenet_meretek[0]), int(bemenet_meretek[1])

adatok = []

for i in range(N):
    sor = bemenet.readline().rstrip()
    sor = sor.split(" ")
    # sor=[int(a) for a in sor]
    # sor= list(map(int, sor))
    for j in range(M):
        sor[j] = int(sor[j])
    adatok.append(sor)

bemenet.close()

kimenet = open("be2_javitott.txt", "a")


for i in range(len(adatok)):
    for j in range(len(adatok[i])):
        adatok[i][j] = str(adatok[i][j])

# print(adatok)

print(" ".join(adatok[0]))

for lista in adatok:
    kimenet.write(" ".join(lista))
    kimenet.write("\n")

kimenet.close()
