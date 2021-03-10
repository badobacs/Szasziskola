N = int(input())
reggel, este = [], []
for _ in range(N):
    a = input().split()
    este.append(int(a[1]))
    reggel.append(int(a[0]))


# A város egy forgalmas pontján N napon keresztül
# minden nap mérték a légszennyeződés mérté-két reggel és este.

# Írjon programot, amelymegadja azon napok számát, és a napok növekvő sorrendjét,
# amikor  az esti érték nagyobb volt, mint az esti értékek átlaga!

N = int(input())
reggel, este = [], []
# az _ speciális változó név
# Akkor használjuk, ha a változó értékét nem akarjuk felhasználni
for _ in range(N):
    a = input().split()
    este.append(int(a[1]))
    reggel.append(int(a[0]))

# print(este)
# print(reggel)

esti_atlag = sum(este)/len(este)

# Programotási tételek kiválogatás
# (pythonra egyszerűsített verzió)
magas = []
for i in range(len(este)):
    if este[i] > esti_atlag:
        magas.append(i+1)

print(len(magas), *magas)
