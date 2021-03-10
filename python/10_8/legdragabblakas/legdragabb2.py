# Egy ingatlanforgalmazó cégtárolja az eladó lakások alapterületét és árát.
# Írj programot,amely megadja alegdrágább lakás sorszámát!

# Második megoldás:
# csak a beolvasás módja változik

N = int(input())
legnagyobb, legnagyobb_index = 0, 0


for i in range(N):
    beolvasott = input().split(" ")
    # speciális értékadás több van egy sorban
    terulet, ar = int(beolvasott[0]), int(beolvasott[1])
    if legnagyobb < ar:
        legnagyobb = ar
        legnagyobb_index = i+1

print(legnagyobb_index)
