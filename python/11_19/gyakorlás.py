
from oop2 import Kutya, Macska


def read_file(filename):
    data = []
    with open(filename, "r") as ofile:
        for sor in ofile:
            a=sor.split(",")
            if (a[0] == "kutya"):
                ujkuyta=Kutya()
                data.append(ujkuyta)
            elif (a[0] == "macska"):
                ujmacska=Macska()
                data.append(ujmacska)
        ofile.close()
    return data


x=read_file("randomfile.csv")
print(*x,sep="\n")
