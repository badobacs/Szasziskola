
# amíg ciklus

i = 0
# Ez a ciklus addig "fut", míg a while után írt kifejezés Igaz
while i < 10:
    print(i)
    # i érték növelése.
    # Az eggyenlőség nem matematikai volta jól látható
    i = i+1
    # Alternatív megoldás i növelésére
    # i+=1

# A lista egy elem gyüjtemény.
lista = [1, 5, 10]

# for ciklussal végig lehet léptetni
# egy lista elemein.
for elem in lista:
    print(elem)

# A listának lekérhatő a hossza a len függvénnyel
lista_hossza = len(lista)

# A lista elemei a lista[] el érhetők el
# Fontos tudni, hogy a lista 0 tól indexel
# Tehát az első elem a 0
# A második az 1 stb.
print(lista[0])
print(lista[1])
print(lista[2])

# range(hossz) egy lista szerű iterable (felsorolható) objektumot készít,
# Amiben szépen 0 tól vannak felsorolva a számok "hossz"-1 ig
# itt a lista_hossza változó értéke 3
# ezért az r elemei a  [0,1,2]
r = range(lista_hossza)

# Ezeken az elemeken végig lehet menni for ciklussal
for i in r:
    # Mivel az i az az eredeti listánk indexein megy,
    # Ezért felhasználható az elemek elérésére lista[i]
    print(str(i)+" dik elem: "+str(lista[i]))
    # Print érdekesség
    # Több paramétert is elfogad, és az úgynevezett sep (separator)
    # Szöveggel választja el őket
    print(i, "dik elem:", lista[i], sep=",")


valmi_szoveg = "Valami szöveg"
# A szöveg típus (str) felsorolható, ezért annak az elemein is végig lehet menni
for char in valmi_szoveg:
    # print függvény end paramétere azt mondja meg,
    # hogy a kiírás után mi legyen az elválasztó karakter
    # Alapértelmezetten ez az új sor.
    print(char, end=" ")
