N = int(input())

jegyek_db = [0, 0, 0, 0, 0]
jegyek = []

for i in range(N):
    jegyek.append(int(input()))

# Alternatív megoldás a jegyekre.
# Használjuk a lista beépített count függvényét
# A count megadja, hogy az adott elemből hány darab található a listában
for i in range(1, 6):
    print(jegyek.count(i), end=" ")

# lista rendezhető a sort függvényével
# Probléma lehet hogy módosítja az eredeti listát, ami így elveszik
# jegyek.sort()
print(*jegyek)

# Rendezés alternatív megoldása: sorted függvény
# A sorted fv nem módosítja az eredeti listát.
rendezett_jegyek = sorted(jegyek)
print(*jegyek)
print(*rendezett_jegyek)

# Érdekesség: mivel a szöveg is egy felsorolható objektum,
# Ezért azon is működik a sorted függvény
# a * és a sep="" csak a szép kiíráshoz kell.
print(*sorted("töltöttkáposzta"), sep="")
