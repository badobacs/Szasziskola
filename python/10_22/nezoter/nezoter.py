def read_file(filename):
    kateg_file = open(filename, "r")
    data = []
    for _ in range(15):
        sor = kateg_file.readline().strip()
        data.append(sor)
    return data

# feladat 1
foglaltsag = read_file("forras/foglaltsag.txt")
kategoriak = read_file("forras/kategoria.txt")




# print(foglaltsag)
# print(kategoriak)
# feladat 2

def feladat_2():
    print("feladat 2")
    f2_sor = int(input("sor szam:"))
    f2_szek = int(input("szek szam:"))

    if foglaltsag[f2_sor-1][f2_szek-1]=="x":
        print("foglalt")
    else:
        print("szabad")


feladat_2()

