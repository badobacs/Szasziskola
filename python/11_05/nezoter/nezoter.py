def read_file(filename):
    with open(filename, "r") as kateg_file:
        data = []
        for _ in range(15):
            sor = kateg_file.readline().strip()
            data.append(sor)
        kateg_file.close()
    return data


def feladat_2(foglaltsag):
    print("feladat 2")
    f2_sor = int(input("sor szam:"))
    f2_szek = int(input("szek szam:"))

    if foglaltsag[f2_sor-1][f2_szek-1] == "x":
        print("foglalt")
    else:
        print("szabad")


def feladat_3(foglaltsag):
    print("feladat 3")
    szamlalo = 0
    osszes = 0
    for sor in foglaltsag:
        for szek in sor:
            osszes += 1
            if szek == "x":
                szamlalo += 1
    szazalek = round(szamlalo/osszes*100)
    szazalek = int(szazalek)
    print(
        f"Az előadásra eddig {szamlalo} jegyet adtak el, ez a nézőtér {szazalek}%-a.")


def feladat_4_5(foglaltsag, kategoriak):
    print("feladat 4")
    kategoria_szamlalo = [0]*5
    for i in range(15):
        for j in range(20):
            kat = int(kategoriak[i][j])
            fogl = foglaltsag[i][j]
            if fogl == "x":
                kategoria_szamlalo[kat-1] += 1
    max_ert = max(kategoria_szamlalo)
    max_ind = kategoria_szamlalo.index(max_ert)+1
    print(f"A legtöbb jegyet a(z) {max_ind}. árkategóriában értékesítették.")
    print("feladat 5")
    kategoria_ar = [5000, 4000, 3000, 2000, 1500]
    bevetel = 0
    for i in range(5):
        bevetel += kategoria_ar[i]*kategoria_szamlalo[i]
    print(bevetel)


def egyedulallo(sor, index):
    # if sor[index] == "x":
    #     return False
    # if index > 0 and sor[index-1] == "o":
    #     return False
    # if index < len(sor)-1 and sor[index+1] == "o":
    #     return False
    # return True
    return not (sor[index] == "x" or
                index > 0 and sor[index-1] == "o" or
                index < len(sor)-1 and sor[index+1] == "o")


def feladat_6(foglaltsag):
    print("feladat 6")
    szamlalo = 0
    for sor in foglaltsag:
        for i in range(20):
            if egyedulallo(sor, i):
                szamlalo += 1
    print(szamlalo)


def feladat_7(foglaltsag, kategoriak):
    with open("szabad.txt", "w") as kimenet:
        for i in range(len(foglaltsag)):
            for j in range(len(foglaltsag[0])):
                fogl = foglaltsag[i][j]
                kat = kategoriak[i][j]
                if(fogl == "x"):
                    kimenet.write("x")
                else:
                    kimenet.write(kat)
            kimenet.write("\n")


if __name__ == "__main__":
    # feladat 1
    foglaltsag = read_file("forras/foglaltsag.txt")
    kategoriak = read_file("forras/kategoria.txt")
    feladat_2(foglaltsag)
    feladat_3(foglaltsag)
    feladat_4_5(foglaltsag, kategoriak)
    feladat_6(foglaltsag)
    feladat_7(foglaltsag, kategoriak)
