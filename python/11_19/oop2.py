class ALlat:
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


class HaziALlat(ALlat):
    def __init__(self, nev="", nem=""):
        super().__init__()
        self.nev = nev
        self.nem = nem

    def hang(self):
        return ""

    def adj_ki_hangot(self):
        print(type(self))
        print(self.hang())
    def __str__(self) -> str:
        return f"nev:{self.nev} nem{self.nem} kor:{self.kor} suly:{self.suly}"



class Kutya(HaziALlat):
    def __init__(self, nev='', nem=''):
        super().__init__(nev=nev, nem=nem)

    def hang(self):
        return "wau"


class Macska(HaziALlat):
    def __init__(self, nev='', nem=''):
        super().__init__(nev=nev, nem=nem)

    def hang(self):
        return "miau"

# class SajatLista(list):
#     def atlag(self):
#         return sum(self)/len(self)

# l=[1,2,3]

# l=SajatLista([1,2,3])
# print(l.atlag())


if __name__=="__main__":
    fifi = Kutya()

    fifi.adj_ki_hangot()
    m = Macska("pötyi", "f")

    m.adj_ki_hangot()
    print(ALlat.db)
    print(fifi.suly)


    def osszead(a: int, b: int):
        return a+b
    # osszead(fifi, m)

    def akarmi(a:HaziALlat):
        a.adj_ki_hangot()

    akarmi(fifi)


