bemenet = input().split()
varosok_szama, napok_szama, homerseklet = int(
    bemenet[0]), int(bemenet[1]), int(bemenet[2])

lista = []

for _ in range(varosok_szama):
    bemenet = input().split()
    counter = 0
    for i in bemenet:
        if int(i) > homerseklet:
            counter += 1
    lista.append(counter)

max_value = max(lista)
print(lista.index(max_value))