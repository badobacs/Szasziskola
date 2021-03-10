N = int(input())
V_kat = 0
VI_kat = 0
VII_kat = 0
for i in range(N):
    varos = input()
    lelekszam = int(input())
    indulok = int(input())

    if lelekszam >= 8000 and lelekszam < 25000:
        V_kat += 1
    elif lelekszam >= 25000 and lelekszam < 70000:
        VI_kat += 1
    elif lelekszam >= 70000:
        VII_kat += 1

# print (V_kat, VI_kat, VII_kat)


if V_kat:
    print("VAN ", end="")
else:
    print("NINCS ", end="")
if VI_kat:
    print("VAN ", end="")
else:
    print("NINCS ", end="")
if VII_kat:
    print("VAN ", end="")
else:
    print("NINCS ", end="")
