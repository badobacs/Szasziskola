# Mester -> kezdő -> progtételek megszámlálás -> 14. jegyek feladat

# Ismerjük egy egyetemi évfolyam vizsgajegyeit.
# Számold meg, hogy az 1, 2, 3, 4 és 5-ös jegyekből külön-külön hány darab van!

# Bemenet
# A standard bemenet első sorában található az évfolyam tagjainak száma (1≤N≤100). Az
# ezt követő N sorban az évfolyam jegyei vannak (1, 2, 3, 4 vagy 5 értékek).

# Kimenet
# A standard kimenet egyetlen sorába ki kell írni szóközzel elválasztva 5 számot, melyek
# értékei az egyes jegyek darabszámai 1-től 5-ig!


# Beolvassuk az N értékét és inté konvertáljuk
N = int(input())

# Létrehozunk egy üres listát. Ebben fogjuk tárolni a beolvasott jegyeket
jegyek = []

# Kell egy ciklus ami N szer ismétlődik meg (Ennyi darab jegyünk van)
for i in range(N):
    # A lista append metódusa hozzáfűz egy elemet a lista végéhez
    # Ez az új elem az int(input()) ami az éppen beolvasott szám
    jegyek.append(int(input()))

# Szeretnénk leszámolni hogy melyik jegyből hány darab van
# Erre létrehozunk egy 0 ból álló 5 elemű listát
jegyek_db = [0, 0, 0, 0, 0]

# Alternatív 5 elemű lista létrehozás.
# jegy_db=[0]*5

# Végig megyünk a beolvasott jegyeken
for jegy in jegyek:
    # Megnöveljük az aktuális jegy darabszámát
    # Fontos a jegy-1 kifejezés, mivel a lista 0 tól számoz!
    jegyek_db[jegy-1] += 1

# Jegyek számának kiírása Mint lista (csak teszteléshez)
# print(jegyek_db)

# Jegyek számának kiírása ciklussal
for jegy_db in jegyek_db:
    # a feladat szövege szerint egy sorva spaceval elválasztva kell (end=" ")
    print(jegy_db, end=" ")

# Alternatív kiírás spread operátorral "*" karakter a tömb neve elött
# spread operator. Szét dobja elemeire a tömböt
# (
#   ha a tömb [1, 2, 3] volt akkor gyakorlatilag három különálló adatot csinál belőle
#   print(*[1,2,3]) körülbelül olyan mintha print(1,2,3) lenne
# )
# Így a jegyek darabszámait a print "sep" el elválasztva írja ki, ami alapértelmezetten space

# print(*jegyek_db)


# alternatív félkész megoldás a jegyek megszámolására
# j1, j2, j3, j4, j5 = 0, 0, 0, 0, 0
# for jegy in jegyek:
# if jegy == 1:
#     j1+=j1
# elif jegy == 2:
#     j2+=j2
