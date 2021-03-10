bemenet_meretek = input().split()
N, M = int(bemenet_meretek[0]), int(bemenet_meretek[1])

adatok = []

for i in range(N):
    sor = input().rstrip()
    sor = sor.split(" ")
    for j in range(M):
        sor[j] = int(sor[j])
    adatok.append(sor)

maximum = sum(adatok[0])/len(adatok[0])
maximum_index = 0
for i in range(N):
    lista = adatok[i]
    aktualis = sum(lista)/len(lista)
    if aktualis > maximum:
        maximum = aktualis
        maximum_index = i

print(maximum_index+1)


atlagok = []
for lista in adatok:
    atlagok.append(sum(lista)/len(lista))

maximum_index2 = atlagok.index(max(atlagok))

print(maximum_index2+1)


# print(*adatok, sep='\n')
