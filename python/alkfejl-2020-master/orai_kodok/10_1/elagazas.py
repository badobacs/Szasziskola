#kor = input("Add meg a korod\n")
#kor = int(kor)

# Lehet rögtön a beolvasott szöveget számmá konvertálni
kor = int(input("Add meg a korod\n"))


# Egyszerű elágazás
# Logikai típust vár
# A <,>,<=,>= ... Operátorok mind értelmesek
# Teljes listáért keress rá
# if kor < 18:
#     print("kiskorú")
# else:
#     print("nagykorú")


# többszörös elágazás is lehet az első igazra "matchel"
# A többit figyelmen kívül hagyja
if kor < 6:
    print("Kisgyerek")
elif kor < 18:
    print("Kiskorú")
elif kor < 65:
    print("nagykorú")
else:
    print("nyugdíjas")

# Logikai típus értéke lehet True és False
vezet = True
# vezet=False

# egymásba ágyazhatók az elágazások
if kor < 18:
    print("nem ihat")
else:
    if vezet:
        print("nem ihat")
    else:
        print("Ihat")
# Ennél a példánál nem szép, mert többször
# Ugyanaz a kimenet print("nem ihat")

# Bonyolultabb logikai kifejezések írhatók az
# "and" és az "or" szavak használatával ("és", "vagy")
if kor < 18 or vezet:
    print("nem ihat")
else:
    print("Ihat")

# Az eggyenlőség vizsgálat a ==
# A nem eggyenlő a !=
if kor < 18 or vezet == True:
    print("nem ihat")
else:
    print("Ihat")
