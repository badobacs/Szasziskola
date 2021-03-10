from oop2 import Kutya, Macska


def read_file(filename):
    data = []
    with open(filename, "r") as ofile:
        for sor in ofile:
            a = sor.strip().split(",")
            if (a[0] == "kutya"):
                ujkuyta = Kutya(nev=a[1], nem=a[2])
                # ujkuyta.nev=a[1]
                # ujkuyta.nem=a[2]
                ujkuyta.kor = int(a[3])
                ujkuyta.suly = int(a[4])
                data.append(ujkuyta)
            elif (a[0] == "macska"):
                ujmacska = Macska()
                ujmacska.nev = a[1]
                ujmacska.nem = a[2]
                ujmacska.kor = int(a[3])
                ujmacska.suly = int(a[4])
                data.append(ujmacska)
        ofile.close()
    return data

# kor=[]
# nev=[]

# ind=kor.index(max(kor))
# legidosebb_nev=nev[ind]


x = read_file("data.csv")
# print(*x,sep="\n")

# print("\n\n\n kor szerint rendezve")

# x.sort(key=lambda allat:allat.kor)
# print(*x,sep="\n")


# 1. Írd ki a legkönnyebb állat adatait,

legkonnyeb = min(x, key=lambda a: a.suly)

print(legkonnyeb)

# 2. Válogasd ki azokat az állatokat, amelyek idősebbek 5 nél

idosek = filter(lambda a: a.kor > 5, x)

print("Idős állatok")
print(*idosek, sep="\n")

# 2. Az 5 évesnél idősebb tíz évesnél fiatalabb legkisebb súlya

lista = filter(lambda a: a.kor > 5 and a.kor < 10, x)
legk = min(lista, key=lambda a: a.suly)

print(legk)
