# Program beolvas nevet életkort és megmondja
# 10 év múlva hány éves lesz

# Az input függvény kiírja a consolra, amit beleírunk,
# És beolvassa, amit a felhasználó gépel a következő enter lenyomásáig
beolvasott_nev = input("Kérlek Írd be a neved\n")
beolvasott_kor = input("Kérlek írd be a korod\n")

# A beolvasott_kor str (szöveg típusú),
# hogy össze lehessen adni számként át kell alakítani
# Az int az egész típus
tiz_ev_mulva = int(beolvasott_kor) + 10

kimenet = "Tíz év múlva " + str(tiz_ev_mulva) + " idős leszel"
print("Hello " + beolvasott_nev)
print(kimenet)
