
def szam_beolvasas():
    a=0
    while True:
        try:
            a = int(input())
            break
        except Exception as e:
            print("Nem szamot adtal meg")
    return a


def ossztas_vizsgalat(osztando, oszto):
    if(osztando % oszto == 0):
        print("oszthato")
    else:
        print("nem oszthato")


print("add meg melyik szám oszthatóságát szeretnéd vizsg...")
osztando = szam_beolvasas()
print("melyik szammal..")
a = szam_beolvasas()
while a != 0:
    ossztas_vizsgalat(osztando, a)
    print("melyik szammal..")
    a = szam_beolvasas()



