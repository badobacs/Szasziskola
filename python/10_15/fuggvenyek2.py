# csinálj függvényt, ammi a faktoriális értékét adja vissza.
# 5->1*2*3*4*5 (120)

def faktorialis(n):
    szorzat = 1
    for i in range(1, n+1):
        # szorzat*=i
        szorzat = szorzat*i
    return szorzat

# rekurzió (ez nem kell)


def fakt2(n):
    if(n == 1):
        return 1
    return n*fakt2(n-1)


print(faktorialis(10))
print(fakt2(10))

# Csináld meg a maimum függvényt ami egy listát kap,
# és visszaadja a legnagyobb elemet

lista = [-5, 5, 10, 33, 0, 2, -350]


def maximum(lista2):
    legnagyobb = lista2[0]
    for l in lista2:
        if l > legnagyobb:
            legnagyobb = l
    return legnagyobb


print(maximum(lista))

a = 2

# nem Növeli meg
def novel(a):
    a += 1


novel(a)

print(a)

