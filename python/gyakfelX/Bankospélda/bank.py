bemenet = input().split(" ")
esemenyek_szama, vizsgalt_idopont = int(bemenet[0]), int(bemenet[1])

counter = 0

for _ in range(esemenyek_szama):
    esemenyek = input().split(" ")
    idopont, esemeny = int(esemenyek[0]), int(esemenyek[2])
    if vizsgalt_idopont > idopont and esemeny == 1:
        counter += 1

print(counter)