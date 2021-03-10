class vizallas(object):
    def __init__(self,ev,viz,telep,folyo):
        self.ev=ev
        self.viz=viz
        self.telep=telep
        self.folyo=folyo

    def __str__(self):
        return f"{self.ev}, {self.viz}, {self.telep}, {self.folyo}"

vizallasok=[]
telepulesek=[]


with open("vizallas.txt","r") as file:
    for sor in file:
        sor=sor.rstrip().split()
        akt=vizallas(sor[0],int(sor[1]),sor[2],sor[3])
        vizallasok.append(akt)
        telepulesek.append(akt.telep)
        # print(akt)




print("feladat 1")

print(f"{len(vizallasok)} db adat van")

print("feladat 2")

egyedi_telepulesek = set(telepulesek)

print(len(egyedi_telepulesek))


print("feladat 3")
max_vizallas=max(vizallasok,key=lambda v:v.viz)
print(f"A {max_vizallas.viz} volt a legnagyob a {max_vizallas.folyo} folyón")


print("feladat 4")

datum=input("Add meg a keresett evet: ").strip()

keresett_adatok=list(filter(lambda v:v.ev==datum,vizallasok))

with open("ki.txt", "w") as ofile:
    for sor in  keresett_adatok:
        sor_str=f"{sor.ev}\t{sor.viz}\t{sor.telep}\t{sor.folyo}\n"
        ofile.write(sor_str)
    ofile.close()
