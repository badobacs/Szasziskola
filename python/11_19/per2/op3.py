class Allat:
    """
    Az állatok osztály egy állat objektumot reprezentál
    """
    db = 0

    def __init__(self):
        self.db += 1
        self.suly = 0
        self.labak_szama = 0
        self.kor = 0
        self.tud_falra_maszni = False

    def __del__(self):
        self.db -= 1


class HaziAllat(Allat):
    def __init__(self, nev="", nem=""):
        super().__init__()
        self.nev = nev
        self.nem = nem
    def hang(self):
        return ""


class Kutya(Allat):
    def __init__(self, nev="", nem=""):
        super().__init__(nev=nev, nem=nem)
    def hang(self):
        return "wau"
    def adj_ki_hangot():
        print(self.hang())
    

class Macska(Allat):
    def __init__(self, nev="", nem=""):
        super().__init__(nev=nev, nem=nem)
    def hang(self):
        return "miau"
    


fifi = Kutya()

fifi.adj_ki_hangot()
m=Macska

print(Allat.db)
print(fifi.suly)
