# Egy ingatlanforgalmazó cégtárolja az eladó lakások alapterületét és árát.
# Írj programot,amely megadja alegdrágább lakás sorszámát!

# első megoldás:
# Programozási tétellel (Maximum kiválasztás)

N = int(input())
legnagyobb = 0
legnagyobb_index = 0
for i in range(N):
    # az input sor végéig olvas egy szöveget
    # ebben nekünk több adatunk van " " karakterrel elválasztva
    a = input()
    # a split függvény a szöveget "szétszedi" a megadott elválasztó karaktereknél
    # és egy szövegeket tartalmazó listát csinál belőle.
    a = a.split(" ")
    # Mivel nekünk csak az ár kell ezért csak az a[1]- el foglalkozunk
    # (ez a második oszlop)
    ar = int(a[1])
    if legnagyobb < ar:
        legnagyobb = ar
        legnagyobb_index = i+1

print(legnagyobb_index)
