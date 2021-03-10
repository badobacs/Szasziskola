# python függvény
# def függvény_neve(paraméterek):

def osszead(a, b):
    # a return kulcsszó után szerepel az az érték vagy kifejezés,
    # ami a függvény "eredménye" lesz.
    return a+b


# tehát az osszead(1,2) -> 1+2 -> 3 helyettesítődik be
print(osszead(1, 2))


# írj egy fuggvenyt ami kap két számot a-t és b-t
# majd összeadja az a-és b közti számokat

def osszegzes(a, b):
    # a függvényen belül nem csak a return lehet
    osszeg = 0
    for i in range(a+1, b):
        osszeg += i
    return osszeg


ab_kozti_szamok_osszege = osszegzes(1, 9)
print(ab_kozti_szamok_osszege)


def osszegzes2(a, b):
    # sok beépített függvény van a pythonban
    # sum összeadja egy felsorolható "dolog" (lista) elemeinek összegét
    return sum(range(a+1, b))


lista = [1, 5, 3]

print(sum(lista))
# Len függvény viszaadja a lista hosszát, korábban használtuk
print(sum(lista)/len(lista))

print(min(lista))
print(max(lista))
