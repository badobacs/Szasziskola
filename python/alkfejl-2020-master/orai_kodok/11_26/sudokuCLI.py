import random

class Sudoku():
    def __init__(self, a):
        self.meret = int(len(a)**(1/2))
        self.kezdo_allapot = a

    def print(self):
        for i in range(len(self.kezdo_allapot)):
            c = self.kezdo_allapot[i]
            if c == "0":
                print("_", end=" ")
            else:
                print(c, end=" ")

            if i % self.meret == self.meret-1:
                print()


feladvanyok = []
with open("feladvanyok.txt", "r") as file:
    for sor in file:
        s = Sudoku(sor.strip())
        feladvanyok.append(s)

print(f"3. feladat Beolvasva {len(feladvanyok)} feldavány")

f4_meret=int(input("4. feladat Adj meg egy szamot 4-9 ig: "))
while f4_meret<4 or f4_meret>9:
    f4_meret=int(input("4. feladat Adj meg egy szamot 4-9 ig: "))

f4_feladv=list(filter(lambda f: f.meret==f4_meret, feladvanyok))
print(f"a {f4_meret}x{f4_meret}-ű fela..{len(f4_feladv)}")


random_index=random.randint(0,len(f4_feladv)-1)

print(f"5f a kiv fel:")
random_feladvany=f4_feladv[random_index]
print(random_feladvany.kezdo_allapot)
# print(random.choice(f4_feladv).kezdo_allapot)



r_string=random_feladvany.kezdo_allapot

f6_mo=(len(r_string)-r_string.count("0"))/len(r_string)*100

print(f"6f feldv kitoltottsege: {f6_mo:.0f}")


print(f"7f")
random_feladvany.print()

print("8f")

with open(f"sudoku{f4_meret}.txt", "w") as ofile:
    for f in f4_feladv:
        ofile.write(f.kezdo_allapot)
        ofile.write("\n")


# for f in feladvanyok:
#     f.print()
