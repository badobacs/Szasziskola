import math

class Sodoku():
    def __init__(self,a):
        self.meret=int(len(a)*(1/2))
        self.kezdo_allapot=a
    def print(self):
        for i in range(len(self.kezdo_allapot)):
            print(self.kez_allapot[i],end=" ")
            if i%self.meret==self.meret-1:
                print()
         


a=Sodoku("12223422422112")
print(a.meret)

feladvanyok= []
with open("feladvanyok.txt", "r") as file:
    for sor in file:
        s= Sudoku(sor.strip())
        feladvanyok.append(s)
print(f"")



math.sqrt(9)

9**(1/2)