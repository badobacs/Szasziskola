# feladat írj egy osztályt ami sudokut fog reprezentálni
# adattagok
# kezdoallapot: egy szöveg, ami egy sorban tartalmazza a sudoku állapotát
# meret: a kezdő állapot hosszának gyöke 

import math

class Sudoku():
    def __init__(self, a):
        self.meret = int(len(a)**(1/2))
        self.kezdo_allapot=a


    def print(self):
        for i in range(len(self.kezdo_allapot)):
            c=self.kezdo_allapot[i]
            if c=="0":
                print("_", end=" ")
            else:
                print(c,end=" ")
           
            if i % self.meret==self.meret-1:
                print()


a = Sudoku("0040420000230300")
a.print()
# print(a.meret)
