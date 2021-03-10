N = int(input())

tipusok = []

for _ in range(N):
    tipus = input()
    Db = input()
    if tipus not in tipusok:
        tipusok.append(tipus)

print(len(tipusok))