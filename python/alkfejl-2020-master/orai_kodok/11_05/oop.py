class Macska:
    db = 0
    def __init__(self, nev="", kor=0, szoros=True):
        self.nev = nev
        self.kor=kor
        self.szoros=szoros
        Macska.db += 1

    def __str__(self):
        szoros_szoveg="csupasz"
        if self.szoros:
            szoros_szoveg="szoros"
        return f"Neve: {self.nev} kora: {self.kor} {szoros_szoveg}"
    
    def __del__(self):
        Macska.db -= 1

    def nyavog(self):
        print("Miau")


print(Macska.db)
macska1 = Macska("Teso")
print(Macska.db)
macska1.nyavog()
print(macska1.nev)

macska2=Macska(kor=5,szoros=False)

macska2.nyavog()
print(f"{macska2.kor} éves neve {macska2.nev}")

macska_lista=[]

for i in range(500):
    macs=Macska(f"macska{i}",500-i)
    macska_lista.append(macs)

print(macska1)

print(Macska.db)

del macska1

print(Macska.db)

print(*macska_lista, sep="\n")



def macska_to_kor(macska):
    return macska.kor

macska_lista.sort(key=macska_to_kor)
macska_lista.sort(key=lambda m:m.kor)

nev_szerint_rendezett_macska_lista=sorted(macska_lista,key=lambda x:x.nev)
print(*nev_szerint_rendezett_macska_lista, sep="\n")

# print(*macska_lista, sep="\n")
